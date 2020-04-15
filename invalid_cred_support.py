#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.22
#  in conjunction with Tcl version 8.6
#    Apr 19, 2019 06:32:56 PM IST  platform: Linux

import sys
import login

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

def invalid_cred_handler(top, root):
    # print('invalid_cred_support.invalid_cred_handler')

    root.destroy()
    root = tk.Tk()
    login_tl = login.Login_Toplevel(root)

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
    import invalid_cred
    invalid_cred.vp_start_gui()



