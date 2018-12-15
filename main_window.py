import tkinter as tk


class Window(object):

    def __init__(self):
        self.window_handle = tk.Tk()
        self.window_handle.title('BD Simulater')
        self.window_handle.geometry('200x100')
        # return super(Window, self).__init__()

    def create_label(self):
        self.var = tk.StringVar()  # text_var
        self.label = tk.Label(self.window_handle,
                              textvariable=self.var,    # 标签的文字
                              bg='yellow',     # 背景颜色
                              font=('Arial', 12),     # 字体和字体大小
                              width=15, height=2  # 标签长宽
                              )
        self.label.pack()    # 固定窗口位置
        pass

    def create_button(self):

        self.on_hit = False

        button = tk.Button(self.window_handle,
                           text='hit me',      # 显示在按钮上的文字
                           width=15, height=2,
                           command=self.print_selection)     # 点击按钮式执行的命令

        button.pack()    # 按钮位置
        pass

    def button_listener(self):
        if self.on_hit == False:     # 从 False 状态变成 True 状态
            print("on hit")
            self.on_hit = True
            self.var.set('you hit me')   # 设置标签的文字为 'you hit me'
        else:       # 从 True 状态变成 False 状态
            self.on_hit = False
            self.var.set('')  # 设置 文字为空
    pass

    def create_entry(self):
        self.entry = tk.Entry(self.window_handle, show='*')
        self.entry.pack()
        self.text = tk.Text(self.window_handle, height=2)
        self.text.pack()
        pass

    def create_insert_point_buttom(self):
        self.button1 = tk.Button(self.window_handle, text="insert point",
                                 width=15, height=2, command=self.insert_point)

        self.button1.pack()
        pass

    def create_insert_end_buttom(self):
        self.button2 = tk.Button(self.window_handle, text="insert_end",
                                 width=15, height=2, command=self.insert_end)

        self.button2.pack()
        pass

    def insert_point(self):
        var = self.entry.get()
        self.text.insert('insert', var)

    def insert_end(self):
        var = self.entry.get()
        self.text.insert('end', var)

    def create_listbox(self):
        var2 = tk.StringVar()

        var2.set((11, 22, 33, 44))  # 为变量设置值

        # 创建Listbox

        self.listbox = tk.Listbox(self.window_handle,
                                  listvariable=var2)  # 将var2的值赋给Listbox

        # 创建一个list并将值循环添加到Listbox控件中
        list_items = [1, 2, 3, 4]
        for item in list_items:
            self.listbox.insert('end', item)  # 从最后一个位置开始加入值
        self.listbox.insert(1, 'first')  # 在第一个位置加入'first'字符
        self.listbox.insert(2, 'second')  # 在第二个位置加入'second'字符
        self.listbox.delete(2)  # 删除第二个位置的字符
        self.listbox.pack()
        pass

    def print_selection(self, v):

        #v = self.scale.get()

        self.label.config(text='you have selected ' + self.var.get())

        #self.label.config(text='you have selected ' + self.var.get())

        # value = self.listbox.get(self.listbox.curselection())  # 获取当前选中的文本
        # self.var.set(value)  # 为label设置值
        pass

    def create_radio(self):
        radio1 = tk.Radiobutton(self.window_handle, text='Option A',
                                variable=self.var, value='A',
                                command=self.print_selection)
        radio1.pack()
        pass

    def create_scale(self):
        self.scale = tk.Scale(self.window_handle, label='try me', from_=5, to=11, orient=tk.HORIZONTAL, variable=self.var,
                              length=200, showvalue=0, tickinterval=2, resolution=0.01, command=self.print_selection)
        self.scale.pack()
        pass


if __name__ == "__main__":

    window = Window()

    window.create_label()

    # window.create_button()

    # window.create_entry()

    # window.create_insert_point_buttom()
    # window.create_insert_end_buttom()
    # while(1):

    # window.create_listbox()

    # window.create_radio()

    window.create_scale()

    window.window_handle.mainloop()

    # window.create_labe()

    pass
