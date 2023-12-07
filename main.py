import tkinter as tk
from tkinter import ttk
from tkinter import *
import pyglet
from MyApp import MyApp
import os

if __name__ == "__main__":

    root = tk.Tk()
    my_app = MyApp(root)
    root.title("ESIREM - Inventory system")
    root.iconbitmap(os.path.abspath('img/robot.ico'))
    # root.config(background='#222222')
    # root.attributes('-alpha', 0.5)
    style = ttk.Style(root)

    # THEME
    root.tk.call("source", "forest-dark.tcl")
    root.tk.call("source", "forest-light.tcl")
    style.theme_use("forest-dark")

    # FONT
    pyglet.font.add_file('abnes.otf')

    # HEADER
    header = ttk.Label(root, text="ESIREM", font=("abnes", 20), padding=10)
    header.pack(side="top", fill=X)

    # FOOTER
    footer = ttk.Label(root, text="", font=("source", 6), padding=5)
    footer.pack(side="bottom", fill=X)

    # MAIN
    frame = ttk.Frame(root)
    frame.pack()  # RESPONSIVE

    tabControl = ttk.Notebook(frame)  # ONGLETS
    tabControl.pack(padx=10)
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tab3 = ttk.Frame(tabControl)

    tabControl.add(tab1, text='Login')
    tabControl.add(tab2, text='Sales')
    tabControl.add(tab3, text='Stock')
    tabControl.pack(expand=1, fill="both")

    my_app.load_tab_login(tab1)
    treeview = my_app.load_tab_add_sales(tab2)
    my_app.load_tab_stock(tab3)
    my_app.load_data_sales(treeview)

    root.mainloop()
