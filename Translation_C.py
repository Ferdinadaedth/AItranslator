from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox
from database_init import connection
from words_filter import DFAFilter
from AItranslator import  AIProxyChat
from dialog import *
class SimpleTranslationDictionary:
    def __init__(self):
        self.dictionary = {}
        self.connection = connection
        self.translation_history = []

    def add_word_to_db(self, word, definition):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO translation_c (word, meaning) VALUES (%s, %s)", (word, definition))
        self.connection.commit()

    def normalize_text(self, text):
        return text.lower()
    def load_dictionary_from_db(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT word, meaning FROM translation_c")
        rows = cursor.fetchall()
        for row in rows:
            self.dictionary[row[0]] = row[1]

    def add_word(self):
        self.load_dictionary_from_db()
        #word = simpledialog.askstring("tips", "Enter Chinese Word:")
        root = tk.Tk()
        root.withdraw()  # 隐藏根窗口
        # 创建自定义对话框实例
        dialog = CustomDialog6(root)
        word = dialog.result
        if word == "":
            messagebox.showinfo("tips", "You have not entered anything")
            return
        if word in self.dictionary:
            print(f"{word} already exists in the dictionary.")
            messagebox.showinfo("tips", "The word already exists in the dictionary.")
        else:
            definition = simpledialog.askstring("tips", f"please enter{word}'s English definition:")
            word = self.normalize_text(word)

            self.add_word_to_db(word, definition)
            print(f"Added to dictionary and database: {word}: {definition}")

    def translate_sentence(self):
        self.load_dictionary_from_db()
        #sentence = simpledialog.askstring("tips", "Pleas enter your sentence:")
        root = tk.Tk()
        root.withdraw()  # 隐藏根窗口
        # 创建自定义对话框实例
        dialog = CustomDialog5(root)
        sentence = dialog.result
        if sentence == "":
            messagebox.showinfo("tips", "You have not entered anything")
            return
        sentence = self.normalize_text(sentence)
        translated_sentence = ' '.join([self.dictionary.get(word, word) for word in sentence.split()])
        print(f"Translated Sentence: {translated_sentence}")
        Filter = DFAFilter()
        path = 'sensitive_words.txt'
        Filter.parse(path)
        filtered_translated_sentence = Filter.filter(translated_sentence)
        self.translation_history.append((sentence, filtered_translated_sentence))
        self._trim_history()
        message_content = filtered_translated_sentence.replace("{", "").replace("}", "").replace(",","\n")
        messagebox.showinfo("result", message_content)
        return translated_sentence

    def get_translation_history(self):
        messagebox.showinfo("history", self.translation_history)
        return self.translation_history

    def _trim_history(self):
        if len(self.translation_history) > 10:
            self.translation_history = self.translation_history[-10:]

    def AItranslater(self,choice_mode):
        ai_proxy_chat = AIProxyChat()
        #sentence = simpledialog.askstring("tips", "Please enter your sentences:")
        root = tk.Tk()
        root.withdraw()
        dialog = CustomDialog5(root)
        sentence = dialog.result
        if sentence == "":
            messagebox.showinfo("tips", "You have not entered anything")
            return
        result = ai_proxy_chat.send_request(sentence,choice_mode)
        self.translation_history.append((sentence, result))
        self._trim_history()
        messagebox.showinfo("result", result)