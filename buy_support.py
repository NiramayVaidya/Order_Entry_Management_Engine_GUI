#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.22
#  in conjunction with Tcl version 8.6
#    Apr 12, 2019 11:23:23 AM IST  platform: Linux
#    Apr 12, 2019 11:27:01 AM IST  platform: Linux

import sys
import json
from requestlib import buyRequest
import invalid_size
import invalid_limit

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

def buy_cancel_handler(top, root):
    # print('buy_support.buy_cancel_handler')

    root.destroy()

    sys.stdout.flush()

def buy_ok_handler(top, root):
    # print('buy_support.buy_ok_handler')

    symbol = top.Symbol_Menu_Var.get()
    size = top.Size_Entry.get()
    client = top.Client_Menu_Var.get()
    exchange = top.Exchange_Menu_Var.get()
    counter_party = top.Counter_Party_Menu_Var.get()
    price_instruction = top.Price_Instruction_Menu_Var.get()
    account = top.Account_Menu_Var.get()
    limit = top.Limit_Entry.get()
    tif = top.TIF_Menu_Var.get()
    tif_date = top.Date_Picker.get()

    if int(size) < 0:
        root.destroy()
        root = tk.Tk()
        invalid_size_tl = invalid_size.Invalid_Size(root, 'buy')

    if int(limit) < 0:
        root.destroy()
        root = tk.Tk()
        invalid_limit_tl = invalid_limit.Invalid_Limit(root, 'buy')

    with open('orders.csv', 'a') as of:
        of.write('buy' + ',' + symbol + ',' + size + ',' + client + ',' + 
                exchange + ',' + counter_party + ',' + price_instruction + ',' + 
                account + ',' + limit + ',' + tif + ',' + tif_date + '\n')

    data = {
        "type" : 'buy',
	"transactionID" : "-1",
	"symbol" : symbol,
	"size" : size,
	"client" : client,
	"exchange" : exchange,
	"counterParty"  : counter_party,
        "symbolDescription" : top.Symbol_Description_Entry_Var.get(),
	"priceInstruction"  : price_instruction,
	"clientDescription"  : top.Client_Description_Entry_Var.get(),
	"account"  : account,
	"limit"  : limit,
	"TIF"  : tif
        }
    json_data = json.dumps(data)
    print(buyRequest(json_data))
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
    import buy
    buy.vp_start_gui()




