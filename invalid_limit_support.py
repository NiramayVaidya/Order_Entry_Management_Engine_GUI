#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.22
#  in conjunction with Tcl version 8.6
#    Apr 19, 2019 06:32:56 PM IST  platform: Linux

import sys
import buy
import sell

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

def invalid_limit_handler(top, root, win):
    # print('invalid_limit_support.invalid_limit_handler')

    root.destroy()
    root = tk.Tk()
    if win == 'buy':
        buy_tl = buy.Buy_Toplevel(root)
    elif win == 'sell':
        sell_tl = sell.Sell_Toplevel(root)

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
    import invalid_limit
    invalid_limit.vp_start_gui()



