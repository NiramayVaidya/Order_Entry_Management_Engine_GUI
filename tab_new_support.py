#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.18
#  in conjunction with Tcl version 8.6
#    Apr 22, 2019 01:01:06 AM IST  platform: Linux

import sys

import buy
import sell
import modify
import cancel

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

def buy_handler(top, root):
    # root.destroy()
    root_new = tk.Tk()
    buy_tl = buy.Buy_Toplevel(root_new)

    sys.stdout.flush()

def sell_handler(top, root):
    # root.destroy()
    root_new = tk.Tk()
    sell_tl = sell.Sell_Toplevel(root_new)

    sys.stdout.flush()

def modify_handler(top, root):
    # root.destroy()
    root_new = tk.Tk()
    modify_tl = modify.Modify_Toplevel(root_new)

    sys.stdout.flush()

def cancel_handler(top, root):
    # root.destroy()
    root_new = tk.Tk()
    cancel_tl = cancel.Cancel_Toplevel(root_new)

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
    import tab_new.py
    tab_new.py.vp_start_gui()




