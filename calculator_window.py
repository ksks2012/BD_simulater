import os
import types
from copy import deepcopy
from tkinter import *
from tkinter import ttk

import numpy as np
import pandas as pd
from PIL import Image, ImageTk

import sqlite
from info_frame import *


class Calculate(object):
    def __init__(self):
        self.window_handle = Tk()
        self.window_handle.title('calculate')
        self.window_handle.geometry('2000x1000+300+300')

        self.label_attribute = []

        self.create_frame()

        self.create_button_enter_data()

    def create_frame(self):
        self.frame_main = Frame(self.window_handle, bg="blue")
        self.frame_main.grid(sticky='news')

        self.hero_info = []
        self.enermy_info = []

        self.create_info_row(self.hero_info, 0)
        self.create_info_row(self.enermy_info, 1)

        pass

    def create_info_row(self, info_row, row):

        for i in range(4):
            if i == 0:
                info_row.append(
                    Hero_info(master=self.frame_main, window_handle=self.window_handle))
                info_row[i].create_window()
            else:
                info_row.append(Support_info(
                    master=self.frame_main, window_handle=self.window_handle, support=False))
                info_row[i].create_window()

            info_row[i].frame_info.grid(row=row, column=i, sticky='nw')

        com_value = StringVar()
        combox_list = ttk.Combobox(self.frame_main, textvariable=com_value)
        combox_list["values"] = ('1', '2', '3', '4', '5', '6')
        combox_list.current(0)
        combox_list.bind("<<ComboboxSelected>>", self.go)
        combox_list.grid(row=row, column=5, sticky='nw')
        pass

    def go(self, *args):  # 处理事件，*args表示可变参数
        print(comboxlist.get())  # 打印选中的值

    def create_button_enter_data(self):
        self.button_enter = Button(self.window_handle,
                                   text='Enter',
                                   # width=50, height=50,
                                   command=self.button_enter_data_listener)
        self.button_enter.grid(row=2, column=0, sticky='news')
        pass

    def button_enter_data_listener(self):
        print("button_enter_data onhit")
        self.create_result(self.hero_info, 0)
        self.create_result(self.enermy_info, 1)
        pass

    def create_result(self, info_row, row):
        info_row.append(Result_info(
            master=self.frame_main, hero_info=info_row, window_handle=self.window_handle, support=False))
        info_row[-1].create_window()
        info_row[-1].frame_info.grid(row=row, column=4, sticky='nw')
        pass

    pass


if __name__ == "__main__":

    calculate = Calculate()

    calculate.window_handle.mainloop()
