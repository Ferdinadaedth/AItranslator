import tkinter as tk
import tkinter.simpledialog as sd
class CustomDialog0(sd.Dialog):
    def body(self, master):
        self.title("请选择模式         ferdinand翻译程序")  # 设置对话框标题
        self.label = tk.Label(master, text="1 - 中译英，2 - English to Chinese")
        self.label.pack()

        # 调整 Entry 控件的宽度和高度
        self.entry = tk.Entry(master, width=50, bd=5)  # 设置边框宽度和样式
        self.entry.pack(pady=50)  # 增加上下的padding来间接调整高度

    def apply(self):
        self.result = self.entry.get()
class CustomDialog(sd.Dialog):
    def body(self, master):
        self.title("菜单")  # 设置对话框标题
        self.label = tk.Label(master, text="请选择: 1 - 增加单词到词典, 2 - 翻译句子, 3 - Quit, 4 - AI翻译")
        self.label.pack()

        # 调整 Entry 控件的宽度和高度
        self.entry = tk.Entry(master, width=50, bd=5)  # 设置边框宽度和样式
        self.entry.pack(pady=50)  # 增加上下的padding来间接调整高度

    def apply(self):
        self.result = self.entry.get()
class CustomDialog1(sd.Dialog):
    def body(self, master):
        self.title("Menu")  # 设置对话框标题
        self.label = tk.Label(master, text="Choose an option: 1 - Add Word, 2 - Translate Sentence, 3 - Quit， 4 - AItranslator")
        self.label.pack()
        # 调整 Entry 控件的宽度和高度
        self.entry = tk.Entry(master, width=50, bd=5)  # 设置边框宽度和样式
        self.entry.pack(pady=50)  # 增加上下的padding来间接调整高度

    def apply(self):
        self.result = self.entry.get()
class CustomDialog2(sd.Dialog):
    def body(self, master):
        self.title("提示")  # 设置对话框标题
        self.label = tk.Label(master, text="请输入需要翻译的内容:")
        self.label.pack()
        # 调整 Entry 控件的宽度和高度
        self.entry = tk.Entry(master, width=50, bd=5)  # 设置边框宽度和样式
        self.entry.pack(pady=50)  # 增加上下的padding来间接调整高度

    def apply(self):
        self.result = self.entry.get()
class CustomDialog3(sd.Dialog):
    def body(self, master):
        self.title("提示")  # 设置对话框标题
        self.label = tk.Label(master, text="请输入英文单词")
        self.label.pack()
        # 调整 Entry 控件的宽度和高度
        self.entry = tk.Entry(master, width=50, bd=5)  # 设置边框宽度和样式
        self.entry.pack(pady=50)  # 增加上下的padding来间接调整高度

    def apply(self):
        self.result = self.entry.get()
class CustomDialog4(sd.Dialog):
    def body(self, master):
        self.title("提示")  # 设置对话框标题
        self.label = tk.Label(master, text="请输入英文单词")
        self.label.pack()
        # 调整 Entry 控件的宽度和高度
        self.entry = tk.Entry(master, width=50, bd=5)  # 设置边框宽度和样式
        self.entry.pack(pady=50)  # 增加上下的padding来间接调整高度

    def apply(self):
        self.result = self.entry.get()
class CustomDialog5(sd.Dialog):
    def body(self, master):
        self.title("tips")  # 设置对话框标题
        self.label = tk.Label(master, text="Please enter your sentences:")
        self.label.pack()
        # 调整 Entry 控件的宽度和高度
        self.entry = tk.Entry(master, width=50, bd=5)  # 设置边框宽度和样式
        self.entry.pack(pady=50)  # 增加上下的padding来间接调整高度

    def apply(self):
        self.result = self.entry.get()
class CustomDialog6(sd.Dialog):
    def body(self, master):
        self.title("tips")  # 设置对话框标题
        self.label = tk.Label(master, text="Enter Chinese Word:")
        self.label.pack()
        # 调整 Entry 控件的宽度和高度
        self.entry = tk.Entry(master, width=50, bd=5)  # 设置边框宽度和样式
        self.entry.pack(pady=50)  # 增加上下的padding来间接调整高度

    def apply(self):
        self.result = self.entry.get()