#! /usr/bin/env python3
#  -*- coding:utf-8 -*-
###############################################################
# © kenwaldek                        MIT-license
#
# Title: tkinter_menu                Version: 1.0
# Date: 26-12-16                     Language: python3
# Description: tkinter menubar
#
###############################################################

from tkinter import *

class Window(Frame):

    def __init__(self, master = None):
        Frame.__init__(self, master)
        Frame.tkraise(self)  # frame aan de voorkant normaal

        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title('gui')
        self.pack(fill=BOTH, expand=1)
        quit_button = Button(self, text='quit', command=self.client_exit)
        quit_button.place(x=0, y=0)
        # voegt een quit knop toe aan het frame
        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu)
        file.add_command(label='Exit', command= self.client_exit)
        menu.add_cascade(label='File', menu=file)

        edit = Menu(menu)
        edit.add_command(label='Undo') # normaal add je een command=
        menu.add_cascade(label='Edit', menu=edit)


    def client_exit(self):
        exit()


root = Tk()
root.geometry('400x300')
app = Window(root)
root.mainloop()
