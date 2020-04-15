#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.22
#  in conjunction with Tcl version 8.6
#    Apr 19, 2019 11:36:01 AM IST  platform: Linux
#    Apr 19, 2019 11:36:53 AM IST  platform: Linux

import sys
import signup
# import order_fill
import tab_new
import invalid_cred

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def login_handler(top, root):
    # print('login_support.login_handler')

    username = top.Username_Entry.get()
    password = top.Password_Entry.get()

    found = 0
    with open('users.csv', 'r') as uf:
        for line in uf:
            usrnm, pswd = line.split(',')
            if usrnm == username and pswd.strip() == password:
                print('found!')
                found = 1
                break

    if found == 1:
        root.destroy()
        root = tk.Tk()
        # order_fill_tl = order_fill.Main_Toplevel(root)
        tab_tl = tab_new.Toplevel1(root)
    else:
        root.destroy()
        root = tk.Tk()
        invalid_cred_tl = invalid_cred.Invalid_Cred(root)

    sys.stdout.flush()

def signup_handler(top, root):
    # print('login_support.signup_handler')
    
    root.destroy()
    root = tk.Tk()
    signup_tl = signup.Signup_Toplevel(root)

    sys.stdout.flush()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import login
    login.vp_start_gui()





