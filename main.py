import login
import login_support

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

def main():
   root = tk.Tk()
   login_tl = login.create_Login_Toplevel(root)
   root.mainloop()

if __name__ == '__main__':
    main()
