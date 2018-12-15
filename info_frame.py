import os
import types
from copy import deepcopy
from tkinter import *

import numpy as np
import pandas as pd
from PIL import Image, ImageTk

import sqlite


class info_Frame(Frame):
    def __init__(self, master=None, cnf={}, window_handle=None, support=True, **kw):
        self.frame_main = super().__init__(master=master, cnf=cnf, **kw)

        self.label_title_text = ['name', 'type', 'hp', 'atk',
                                 'defen', 'CT_rate', 'CT_bonus', 'dex']

        self.label_attribute = [None, None, None, None, None, None, None, None]

        self.select_image = None

        self.window_handle = window_handle
        self.support = support

    def create_window(self):
        self.create_frame()

        self.create_button_select()
        self.create_data_label()

        # self.cal_result()

    def create_frame(self):
        # Create a frame for the canvas with non-zero row&column weights
        self.frame_info = Frame(self.frame_main)
        # self.frame_info.grid(row=2, column=0, pady=(5, 0), sticky='nw')
        self.frame_info.grid_rowconfigure(0, weight=1)
        self.frame_info.grid_columnconfigure(0, weight=1)
        # Set grid_propagate to False to allow 5-by-5 buttons resizing later
        # self.frame_info.grid_propagate(False)

        # Add a canvas in that frame
        self.canvas = Canvas(self.frame_info, bg="yellow")
        self.canvas.grid(row=0, column=0, sticky="news")

        # Create a frame to contain the buttons
        self.frame_buttons = Frame(self.canvas, bg="white")
        self.canvas.create_window(
            (0, 0), window=self.frame_buttons, anchor='nw')

        # frame for attribute title(label)
        self.frame_lable_title = Frame(self.frame_info, bg="red")
        self.frame_lable_title.grid(row=1, column=0, sticky="news")
        pass

    def create_button_select(self):

        self.select_button = Button(self.canvas, text='Select',
                                    # width=120, height=120,
                                    command=self.button_select_listener)
        self.select_button.grid(row=0, column=0,
                                padx=0, pady=0, sticky='news')

        pass

    # (C)
    def button_select_listener(self):
        print("on hit")

        try:
            select = Select_hero(self.window_handle, self.support)
            self.window_handle.wait_window(select.window_handle)
            self.click_data = select.click_data

            self.update_after_buttom_onClick()
        except:
            print("close")
        pass

    def create_data_label(self):

        for i in range(8):
            Label(self.frame_lable_title,
                  text=self.label_title_text[i],
                  # bg='yellow',
                  font=('Arial', 12),
                  width=15, height=2,
                  ).grid(row=i, column=0)

        pass

    # (M)
    def update_after_buttom_onClick(self):
        print(self.click_data)
        # update picture
        url = self.click_data['url'].values[0]
        # url = self.click_data['url'].value(0)
        print(url)
        self.select_image = ImageTk.PhotoImage(Image.open(url))
        self.select_button.config(text='', image=self.select_image)

        # update label
        click_data_show = []
        for i in range(8):
            click_data_show.append(
                # self.click_data[self.label_title_text[0]].values[0])
                self.click_data[self.label_title_text[i]].values[0])

            # self.click_data[['name', 'type', 'atk', 'hp', 'defen', 'CT_rate', 'CT_bonus', 'dex']]
        print(click_data_show[0])
        for i in range(8):
            # label_text = 'error'

            if not (isinstance(click_data_show[i], str)):
                self.label_attribute[i] = (str(click_data_show[i]))
            else:
                self.label_attribute[i] = (click_data_show[i])

            Label(self.frame_lable_title,
                  text=self.label_attribute[i],
                  # bg='yellow',
                  font=('Arial', 12),
                  width=15, height=2,
                  ).grid(row=i, column=1)
            pass

        pass


class Hero_info(info_Frame):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master=master, cnf=cnf, **kw)

    def get_select_image(self, select_image):
        select_image.append(self.select_image)
        pass


class Support_info(info_Frame):
    def __init__(self, master=None, cnf={}, **kw):
        # self.frame_main = super().__init__(master=master, cnf=cnf, **kw)
        super().__init__(master=master, cnf=cnf, **kw)

        self.label_title_text = ['name', 'type', 'atk', 'atk_inc',
                                 'def_inc', 'CT_rate_inc', 'CT_bonus_inc', 'dex_inc']

        self.create_frame()

        self.create_button_select()
        self.create_data_label()

    def create_data_label(self):

        for i in range(8):
            Label(self.frame_lable_title,
                  text=self.label_title_text[i],
                  # bg='yellow',
                  font=('Arial', 12),
                  width=15, height=2,
                  ).grid(row=i, column=0)

        pass

    # (M)
    def update_after_buttom_onClick(self):
        print(self.click_data)
        # update picture
        url = self.click_data['url'].values[0]
        # url = self.click_data['url'].value(0)
        # print(url)
        self.select_image = ImageTk.PhotoImage(Image.open(url))
        self.select_button.config(text='', image=self.select_image)

        # update label
        click_data_show = []
        for i in range(3):
            click_data_show.append(
                self.click_data[self.label_title_text[i]].values[0])

        self.skill = sqlite.get_support_skill(self.click_data['id'].values[0])
        print(self.skill)

        # (M) get skill
        for i in range(5):
            click_data_show.append(
                self.skill[self.label_title_text[i+3]].values[0])

        print(click_data_show[0])
        for i in range(8):
            # label_text = 'error'

            if not (isinstance(click_data_show[i], str)):
                self.label_attribute[i] = (str(round(click_data_show[i], 4)))
            else:
                self.label_attribute[i] = (click_data_show[i])

            Label(self.frame_lable_title,
                  text=self.label_attribute[i],
                  # bg='yellow',
                  font=('Arial', 12),
                  width=15, height=2,
                  ).grid(row=i, column=1)
            pass

        pass


class Result_info(info_Frame):
    def __init__(self, master=None, cnf={}, hero_info=None, **kw):
        # self.frame_main = super().__init__(master=master, cnf=cnf, **kw)
        super().__init__(master=master, cnf=cnf, **kw)
        # self.frame_main = super().__init__(master=master, cnf=cnf, **kw)

        self.hero_info = hero_info

        pass

    def create_window(self):
        self.create_frame()
        self.create_canvas_head()

        self.create_data_label()

        self.cal_result()
        self.show_result()

    def create_canvas_head(self):

        self.select_image = []
        self.hero_info[0].get_select_image(self.select_image)
        # print(self.hero_info[0].get_select_image())
        # self.select_image[0].show()
        self.canvas_head = Canvas(
            self.canvas, width=120, height=120, bg='green')
        # self.canvas, bg='green')
        self.canvas_head.create_image(
            0, 0, anchor='nw', image=self.select_image[0])
        self.canvas_head.grid(row=0, column=0, padx=0, pady=0, sticky='news')
        pass

    def cal_result(self):

        self.result_attribute = []

        self.label_attribute = self.hero_info[0].label_attribute
        print(self.label_attribute)

        for i in range(3, 8, 1):
            for j in range(1, 2, 1):
                print('hero_info', i, j, type(
                    self.hero_info[j].label_attribute[i]), self.hero_info[j].label_attribute[i])
                if i != 3:
                    try:
                        self.result_attribute.append(round(float(self.label_attribute[i]) + float(self.hero_info[j].label_attribute[2]) * float(
                            self.hero_info[j].label_attribute[i]), 2))
                    except TypeError as e:
                        print(e)
                else:
                    try:
                        self.result_attribute.append(round(float(self.label_attribute[i]) * (1 + float(self.hero_info[j].label_attribute[2]) * float(
                            self.hero_info[j].label_attribute[i])), 2))
                    except TypeError as e:
                        print(e)
        print(self.result_attribute)
        pass

    def show_result(self):
        print(self.result_attribute)
        for i in range(8):
            # label_text = 'error'
            try:
                if i > 2:
                    idx = i - 3
                    print(self.result_attribute[idx])

                    self.label_attribute[i] = str(self.result_attribute[idx])
                else:
                    self.label_attribute[i] = self.hero_info[0].label_attribute[i]

                Label(self.frame_lable_title,
                      text=self.label_attribute[i],
                      # bg='yellow',
                      font=('Arial', 12),
                      width=15, height=2,
                      ).grid(row=i, column=1)
            except IndexError as e:
                print(e)
            pass

        pass


class Select_hero(object):
    def __init__(self, top, support=True):
        self.window_handle = Toplevel(top)
        self.window_handle.title('select')
        self.window_handle.geometry('769x756+100+100')

        self.window_handle.resizable(False, False)
        self.window_handle.wm_attributes('-topmost', 1)

        self.window_handle.grid_rowconfigure(0, weight=1)
        self.window_handle.columnconfigure(0, weight=1)

        self.support = support

        self.button_list = []
        self.photo_list = []
        self.id = []

        # grid frame
        self.create_frame()
        self.create_button()

    pass

    def create_frame(self):
        self.frame_main = Frame(self.window_handle, bg="gray")
        self.frame_main.grid(sticky='news')

        # Create a frame for the canvas with non-zero row&column weights
        self.frame_canvas = Frame(self.frame_main)
        self.frame_canvas.grid(row=2, column=0, pady=(5, 0), sticky='nw')
        self.frame_canvas.grid_rowconfigure(0, weight=1)
        self.frame_canvas.grid_columnconfigure(0, weight=1)
        # Set grid_propagate to False to allow 5-by-5 buttons resizing later
        self.frame_canvas.grid_propagate(False)

        # Add a canvas in that frame
        self.canvas = Canvas(self.frame_canvas, bg="yellow")
        self.canvas.grid(row=0, column=0, sticky="news")

        # Link a scrollbar to the canvas
        self.vsb = Scrollbar(self.frame_canvas, orient="vertical",
                             command=self.canvas.yview)
        self.vsb.grid(row=0, column=1, sticky='ns')
        self.canvas.config(yscrollcommand=self.vsb.set)

        # Create a frame to contain the buttons
        self.frame_buttons = Frame(self.canvas, bg="white")
        self.canvas.create_window(
            (0, 0), window=self.frame_buttons, anchor='nw')

        # doe
        self.window_handle.bind("<Button-4>", self._on_mousewheel)
        self.window_handle.bind("<Button-5>", self._on_mousewheel)

        pass

    def _on_mousewheel(self, event):
        # print("mouse wheel", event.delta, event.num)
        if event.num == 5:
            self.canvas.yview_scroll(5, "units")
        else:
            self.canvas.yview_scroll(-5, "units")

    def create_button(self):

        # (M)
        if self.support == False:
            self.data_df = sqlite.get_all_support_data()
        else:
            self.data_df = sqlite.get_all_data_no_support()

        tatol_rows = len(self.data_df.index)

        url_list = []

        for i in range(tatol_rows):
            url = self.data_df.at[i, 'url']

            image = Image.open(url)

            self.photo_list.append(ImageTk.PhotoImage(image))
            self.id.append(self.data_df.at[i, 'id'])

        columns = 6
        rows = int(tatol_rows / columns) + 1
        for i in range(rows):
            for j in range(columns):
                idx = i * columns + j

                if (idx >= tatol_rows):
                    break

                try:

                    Button(self.frame_buttons,
                           image=self.photo_list[idx],
                           command=lambda _id=self.id[idx]: self.hero_button_listener(
                               _id),
                           ).grid(
                        row=i, column=j,
                        padx=0, pady=0,
                        sticky='news')
                except TclError:
                    print("inpurt png error")
                    pass

        # Update buttons frames idle tasks to let tkinter calculate buttons sizes
        self.frame_buttons.update_idletasks()

        # Resize the canvas frame to show buttons and the scrollbar
        # print(self.vsb.winfo_width())
        self.frame_canvas.config(width=(120+6) * columns + self.vsb.winfo_width(),
                                 height=(120+6)*columns)

        # Set the canvas scrolling region
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

        pass

    # (C)
    def hero_button_listener(self, _id):
        print(_id)
        self.click_data = (self.data_df[self.data_df['id'] == _id])
        self.window_handle.destroy()
        pass
