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
        cursor.execute("INSERT INTO translation (word, meaning) VALUES (%s, %s)", (word, definition))
        self.connection.commit()

    def normalize_text(self, text):
        return text.lower()
    def load_dictionary_from_db(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT word, meaning FROM translation")
        rows = cursor.fetchall()
        for row in rows:
            self.dictionary[row[0]] = row[1]

    def add_word(self):
        self.load_dictionary_from_db()
        #word = simpledialog.askstring("提示", "请输入英文单词")
        root = tk.Tk()
        root.withdraw()

        dialog = CustomDialog3(root)
        word = dialog.result
        if word == "":
            messagebox.showinfo("提示", "您未输入任何内容")
            return

        if word in self.dictionary:
            print(f"{word} already exists in the dictionary.")
            messagebox.showinfo("提示", "词典中已存在该单词")
        else:
            definition = simpledialog.askstring("提示", f"输入{word}的中文解释:")
            if definition == "":
                return
            word = self.normalize_text(word)

            self.add_word_to_db(word, definition)
            print(f"Added to dictionary and database: {word}: {definition}")

    def translate_sentence(self):
        self.load_dictionary_from_db()
        #sentence = simpledialog.askstring("提示", "请输入需要翻译的内容:")
        root = tk.Tk()
        root.withdraw()  # 隐藏根窗口
        # 创建自定义对话框实例
        dialog = CustomDialog2(root)
        sentence = dialog.result
        if sentence == "":
            messagebox.showinfo("提示", "您未输入任何内容")
            return
        sentence = self.normalize_text(sentence)
        translated_sentence = ' '.join([self.dictionary.get(word, word) for word in sentence.split()])
        print(f"Translated Sentence: {translated_sentence}")
        Filter = DFAFilter()
        path = 'sensitive_words.txt'
        Filter.parse(path)
        filtered_translated_sentence = Filter.filter(translated_sentence)
        self.translation_history.append((sentence, filtered_translated_sentence))
        print(self.translation_history)
        self._trim_history()
        messagebox.showinfo("翻译结果", filtered_translated_sentence)
        return translated_sentence

    def get_translation_history(self):

        #messagebox.showinfo("翻译历史", history_str)
        return self.translation_history

    def _trim_history(self):
        if len(self.translation_history) > 10:
            self.translation_history = self.translation_history[-10:]

    def AItranslater(self,choice_mode):
        ai_proxy_chat = AIProxyChat()
        #sentence = simpledialog.askstring("提示", "请输入需要翻译的内容:")
        root = tk.Tk()
        root.withdraw()

        dialog = CustomDialog2(root)

        sentence = dialog.result
        if sentence == "":
            messagebox.showinfo("提示", "您未输入任何内容")
            return
        result = ai_proxy_chat.send_request(sentence,choice_mode)
        print(choice_mode)
        self.translation_history.append((sentence, result))
        self._trim_history()
        messagebox.showinfo("翻译结果", result)