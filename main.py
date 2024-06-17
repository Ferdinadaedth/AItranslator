from tkinter import *
from tkinter import simpledialog
import Translation_E
import Translation_C
from dialog import *
import tkinter as tk

def main():
    #choice_mode = simpledialog.askstring("请选择模式","1 - 中译英，2 - English to Chinese")
    root = tk.Tk()
    root.withdraw()
    dialog = CustomDialog0(root)
    choice_mode = dialog.result
    while True:
        if choice_mode == "1":
            translator = Translation_E.SimpleTranslationDictionary()
            #choice = simpledialog.askstring("菜单","请选择: 1 - 增加单词到词典, 2 - 翻译句子, 3 - Quit， 4 - AI翻译,5 - 翻译历史")
            root = tk.Tk()
            root.withdraw()  # 隐藏根窗口
            # 创建自定义对话框实例
            dialog = CustomDialog(root)
            choice = dialog.result
            if choice == '1':
                translator.add_word()
            elif choice == '2':
                translator.translate_sentence()
            elif choice == '3':
                break
            elif choice == '4':
                translator.AItranslater(choice_mode)
            else:
                print("Invalid choice. Please try again.")
        elif choice_mode == "2":
            translator = Translation_C.SimpleTranslationDictionary()
            #choice = simpledialog.askstring("Menu", "Choose an option: 1 - Add Word, 2 - Translate Sentence, 3 - Quit， 4 - AItranslator,5 - Translation History")
            root = tk.Tk()
            root.withdraw()
            dialog = CustomDialog1(root)
            choice = dialog.result
            if choice == '1':
                translator.add_word()
            elif choice == '2':
                translator.translate_sentence()
            elif choice == '3':
                break
            elif choice == '4':
                translator.AItranslater(choice_mode)
            else:
                print("Invalid choice. Please try again.")



if __name__ == "__main__":
    main()