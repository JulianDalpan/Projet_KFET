"""
@AUTHOR : Joris ZURETTI
@VERSION : 1.0.0

"""

import tkinter as tk
from tkinter import ttk, StringVar, X
import features
import login_library.login as log

class MyApp:

    def __init__(self, root):

        self.root = root
        self.currentSelection = ""
        self.mystr = StringVar()
        self.mystr2 = StringVar()
        self.var = StringVar()
        self.var2 = StringVar()
        self.listQt = []
        self.productList = features.getallitem()
        self.a = tk.BooleanVar()
        self.productList2 = features.getallitem()
        self.quantityList = StringVar()
        self.acces = False
        self.checkbuttonStatus=False

    def load_data_sales(self, treeview):
        """
        This function load all the data for each sales.

        Args : 
            treeview : sales view in tkinter.
        """

        listSales = list(features.getallsale())
        listColumn = list(features.listColumnSales())

        for name in listColumn:
            treeview.heading(name, text=name)

        for valueList in listSales:
            treeview.insert('', tk.END, values=valueList)
    

    def load_data_stock(self):
        """
        This function load all the data for each product in stocks
        """

        listColumn = list(features.listColumnStock())
        all = features.getall()

        for name in listColumn:
            self.treeview2.heading(name, text=name)

        for valueList in all:
            self.treeview2.insert('', tk.END, values=valueList)



    def insert_stock(self):
        """
        This function inserts a product into the current stock
        """
        quantityToAddSpinbox = int(self.quantityToAdd.get())

        if self.checkbuttonStatus:
            
            newProductEntry = self.newProductEntry.get()
            priceOfNewProduct = self.priceOfNewProduct.get()
            purchasedPriceOfNewProduct=self.purchasedPriceOfNewProduct.get()
            features.add_new_items(newProductEntry, priceOfNewProduct, quantityToAddSpinbox,purchasedPriceOfNewProduct)

        else:

            existantProductEntry = self.existantProduct.get()
            features.additems(existantProductEntry, quantityToAddSpinbox)

        # DELETE TREEVIEW
        for item in self.treeview2.get_children():
            self.treeview2.delete(item)

        # RELOAD DATA STOCK
        self.load_data_stock()


    def insert_sales(self):
        """
        This function inserts a product into the current sales
        """
        productEntry = self.product.get()
        quantityEntry = int(self.quantity.get())
        features.addsales(productEntry, quantityEntry)
        rowSalesValue = features.getlastsale()
        # INSERT IN VIEW
        self.treeview.insert('', tk.END, values=rowSalesValue)


    def get_index(self, *args):

        self.currentSelection = self.product.get()
        self.mystr.set(features.getprice(self.currentSelection))

        self.currentSelection2 = self.existantProduct.get()
        self.mystr2.set(features.getprice(self.currentSelection2))

        selected_product = self.var.get()
        print("Selected Product:", selected_product)
        
        self.getquantity = features.getquantity(selected_product)
        print("Get Quantity:", self.getquantity)

        # self.var.trace('w', self.getquantity)

        try:
            self.max_value = self.getquantity
        except AttributeError:
            self.max_value = 0

        self.listQt = self.load_combobox_values(self.max_value)


    def callbackFunc(self):
        """
        This function is enable when an event occurs.
        """
        
        self.currentSelection = self.product.get()
        self.currentSelection2 = self.existantProduct.get()


    def restore_default_text(self, entry, default_text):
        """
        This function restore the default text in each text zone.

         Args :       
            entry (list) : actual text in the text box
            default_text (list) : default text to be placed in the text box
        """

        # INSERT A DEFAULT TEXT
        if entry.get() == "":
            entry.insert(0, default_text)


    def on_product_focus_out(self,event):
        """
        This function allowed to restore the text "Poduct" in the text box.
        """

        if not self.product.get():
            self.product.set("Product")
            
        elif not self.existantProduct.get():
            self.product.set("Product")


    def on_frame_focus_out(self):
        """
        This function allowed to restore the text "Poduct" in the text box.
        """      
        self.var.set("Product")


    def load_combobox_values(self, x):
        """
        This function load the right number list available of the product selected.

        Args :
            x : maximum quantity of the selected product.
        """

        self.listQt = list(range(x + 1)) # Liste de nombres de 0 à x. 
        self.quantity["values"] = self.listQt


    def set_new_product(self):
        """
        This function is used to add a new product to the stock.
        """

        self.checkbuttonStatus = self.a.get()

        if self.checkbuttonStatus:
            self.newProductEntry = ttk.Entry(self.widgets_frame_3)
            self.newProductEntry.insert(0, "Product")
            self.newProductEntry.bind("<FocusIn>", lambda e: self.newProductEntry.delete('0', 'end'))  # EVENT : DELETE LABEL IF FOCUS
            self.newProductEntry.grid(row=1, column=0, sticky="ew", padx=5, pady=5)

            self.priceOfNewProduct = ttk.Entry(self.widgets_frame_3)
            self.priceOfNewProduct.insert(0, "Price")
            self.priceOfNewProduct.bind("<FocusIn>", lambda e: self.priceOfNewProduct.delete('0', 'end'))
            self.priceOfNewProduct.grid(row=2, column=0, sticky="ew", padx=5, pady=5)

            self.purchasedPriceOfNewProduct = ttk.Entry(self.widgets_frame_3)
            self.purchasedPriceOfNewProduct.insert(0, "Purchased Price")
            self.purchasedPriceOfNewProduct.bind("<FocusIn>", lambda e: self.purchasedPriceOfNewProduct.delete('0', 'end'))
            self.purchasedPriceOfNewProduct.grid(row=4, column=0, sticky="ew", padx=5, pady=5)

        else:
            self.newProductEntry.grid_remove()
            self.priceOfNewProduct.grid_remove()


    def load_tab_login(self, tab1,tab2,tab3,tabControl):
        """
        This function load and manage the tab login. 

        Args : 
            tab1 : login tab.
        """

        self.widgets_frame_1 = ttk.LabelFrame(tab1, text="User Login")
        self.widgets_frame_1.pack(fill=X, side="top", padx=350)

        self.image = tk.PhotoImage(file="img/space-invader.png")
        self.image_label = ttk.Label(self.widgets_frame_1, image=self.image).pack()

        self.login = ttk.Entry(self.widgets_frame_1)
        self.login.insert(0, "Login")
        self.login.bind("<FocusIn>", lambda e: self.login.delete('0', 'end'))  # EVENT : DELETE LABEL IF FOCUS
        self.login.bind("<FocusOut>", lambda e: self.restore_default_text(self.login, "Login"))
        self.login.pack(pady=5)

        self.password = ttk.Entry(self.widgets_frame_1,show='*')
        self.password.insert(0, "Password")
        self.password.bind("<FocusIn>", lambda e: self.password.delete('0', 'end'))  # EVENT : DELETE LABEL IF FOCUS
        self.password.bind("<FocusOut>", lambda e: self.restore_default_text(self.password, "Password"))
        self.password.pack(pady=5)

        self.buttonSignIn = ttk.Button(self.widgets_frame_1, text='Sign in',command=lambda:log.login_identify(self.login.get(),self.password.get(),"login_library/utilisateurs.txt",self,tab2,tab3,tabControl))
        self.buttonSignIn.pack(pady=5)

        self.buttonSignIn.focus_set() # INITIAL FOCUS ON BUTTON   


    def load_tab_add_sales(self, tab2):
        
        """
        This function load and manage the tab sales. The view is split in two sides.

        Args : 
            tab2 : sales tab.
        """
        #self.varQ = StringVar()

        # LEFT SIDE #

        self.widgets_frame_2 = ttk.LabelFrame(tab2, text="Add sale(s)")
        self.widgets_frame_2.grid(row=2, column=0, padx=10, pady=10,
                                  sticky="nsew")  # sticky="nsew" = cover all the surface

        self.product = ttk.Combobox(self.widgets_frame_2, textvariable=self.var,
                                     values=self.productList, state="readonly")
        #self.product.insert(0, "Product")
        self.product.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        self.var.set("Product")
        self.var.trace('w', self.get_index)
        self.product.bind("<<ComboboxSelected>>", self.callbackFunc)
        self.product.bind("<FocusIn>", lambda e: self.product.selection_clear())
        self.product.bind("<FocusOut>", self.on_product_focus_out)

        self.varQ = StringVar()

        self.quantity = ttk.Combobox(self.widgets_frame_2, textvariable=self.varQ, values=self.listQt, state="readonly")
        self.varQ.set("Quantity")
        # self.varQ.trace('w', lambda *args: self.load_quantity())
        # self.quantity.insert(0, "Quantity")
        self.quantity.bind("<FocusIn>", lambda e: self.quantity.selection_clear())
        self.quantity.grid(row=1, column=0, sticky="ew", padx=5, pady=5)

        self.price = ttk.Entry(self.widgets_frame_2, textvariable=self.mystr, state='disabled')
        self.price.grid(row=2, column=0, sticky="ew", padx=5, pady=5)

        self.buttonAdd = ttk.Button(self.widgets_frame_2, text='Add', command=lambda: self.insert_sales())
        self.buttonAdd.grid(row=3, column=0, sticky="nsew", padx=5, pady=5)

        self.buttonGeneratePdf = ttk.Button(self.widgets_frame_2, text='Generate PDF', command=lambda: features.generate_sale_pdf())
        self.buttonGeneratePdf.grid(row=4, column=0, sticky="nsew", padx=5, pady=5)

        # RIGHT SIDE #

        self.treeFrame = ttk.Frame(tab2)
        self.treeFrame.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")
        self.treeScroll = ttk.Scrollbar(self.treeFrame)
        self.treeScroll.pack(side="right", fill="y")

        self.cols = ("Product", "Price", "Quantity", "Time")

        self.treeview = ttk.Treeview(self.treeFrame, show="headings",
                                     yscrollcommand=self.treeScroll.set, columns=self.cols, height=13)

        self.treeview.column("Product")
        self.treeview.column("Price")
        self.treeview.column("Quantity")
        self.treeview.column("Time")
        self.treeview.pack(fill=X, padx=10, pady=10)
        self.treeScroll.config(command=self.treeview.yview)

        return self.treeview
    

    def load_tab_stock(self, tab3):
        """
        This function load and manage the tab stock. The view is split in two sides.

        Args : 
            tab3 : stock tab.
        """

        # getprice = features.getprice(self.productList2)

        # LEFT SIDE #
        
        self.widgets_frame_3 = ttk.LabelFrame(tab3, text="Add product(s)")
        self.widgets_frame_3.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
        
        checkbuttonNewProduct = ttk.Checkbutton(self.widgets_frame_3, text = "New product", variable=self.a, command=self.set_new_product)
        checkbuttonNewProduct.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        self.existantProduct = ttk.Combobox(self.widgets_frame_3, textvariable=self.var2,
                                     values=self.productList2, state="readonly")
        self.existantProduct.insert(0, "Product")
        self.existantProduct.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
        self.var2.set("Product")
        self.existantProduct.bind("<<ComboboxSelected>>", self.callbackFunc)
        self.existantProduct.bind("<FocusIn>", lambda e: self.existantProduct.selection_clear())
        self.existantProduct.bind("<FocusOut>", self.on_product_focus_out)

        self.priceExistantProduct = ttk.Entry(self.widgets_frame_3, textvariable=self.mystr2, state='disabled')
        self.priceExistantProduct.grid(row=2, column=0, sticky="ew", padx=5, pady=5) 

        self.quantityToAdd = ttk.Entry(self.widgets_frame_3)
        self.quantityToAdd.insert(0, "Quantity")
        self.quantityToAdd.bind("<FocusIn>", lambda e: self.quantityToAdd.delete('0', 'end'))
        self.quantityToAdd.grid(row=3, column=0, sticky="ew", padx=5, pady=5)

        self.buttonAddProductStock = ttk.Button(self.widgets_frame_3, text='Add', command=lambda: self.insert_stock())
        self.buttonAddProductStock.grid(row=5, column=0, sticky="nsew", padx=5, pady=5)

        # RIGHT SIDE #

        self.treeFrame2 = ttk.Frame(tab3)
        self.treeFrame2.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")
        self.treeScroll2 = ttk.Scrollbar(self.treeFrame2)
        self.treeScroll2.pack(side="right", fill="y")

        cols = ("Product", "Price", "Quantity", "Update")

        self.treeview2 = ttk.Treeview(self.treeFrame2, show="headings",
                                yscrollcommand=self.treeScroll2.set, columns=cols, height=13)
        self.treeview2.column("Product")
        self.treeview2.column("Price")
        self.treeview2.column("Quantity")
        self.treeview2.column("Update")
        self.treeview2.pack(fill=X, padx=10, pady=10)
        self.treeScroll2.config(command=self.treeview2.yview)
        self.load_data_stock()

        return self.treeview2