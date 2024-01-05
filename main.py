"""
@AUTHOR : Joris ZURETTI
@VERSION : 2.1.0

"""

import tkinter as tk
from tkinter import ttk
from tkinter import *
import pyglet
from MyApp import MyApp

if __name__ == "__main__":

    root = tk.Tk()
    my_app = MyApp(root)
    root.title("ESIREM - Inventory system")

    style = ttk.Style(root)

    # THEME
    root.tk.call("source", "Template/forest-dark.tcl")
    style.theme_use("forest-dark")

    # FONT
    pyglet.font.add_file('Template/abnes/abnes.otf')

    # HEADER
    header = ttk.Label(root, text="ESIREM", font=("abnes", 20), padding=10)
    header.pack(side="top", fill=X)

    # FOOTER
    footer = ttk.Label(root, text="", font=("source", 6), padding=5)
    footer.pack(side="bottom", fill=X)

    # MAIN
    frame = ttk.Frame(root)
    frame.pack()

    # ONGLETS
    tabControl = ttk.Notebook(frame)  
    tabControl.pack(padx=10)
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tab3 = ttk.Frame(tabControl)

    tabControl.add(tab1, text='Login')
    tabControl.pack(expand=1, fill="both")

    # LOAD GUI
    my_app.load_tab_login(tab1,tab2,tab3,tabControl)

    root.mainloop()
