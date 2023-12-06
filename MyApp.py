import tkinter as tk
from tkinter import ttk, StringVar, X, Y
import features

class MyApp:

    def __init__(self, root):

        self.root = root
        self.currentSelection = ""
        self.mystr = StringVar()
        self.mystr2 = StringVar()
        self.var = StringVar()
        self.var2 = StringVar()
        self.productList = features.getallitem()
        self.a = tk.BooleanVar()
        self.productList2 = features.getallitem()
        self.quantityList = StringVar()


    def load_data_sales(self, treeview):

        listSales = list(features.getallsale())
        listColumn = list(features.listColumnSales())

        for name in listColumn:
            treeview.heading(name, text=name)

        for valueList in listSales:
            treeview.insert('', tk.END, values=valueList)
    

    def load_data_stock(self):
        listColumn = list(features.listColumnStock())
        all = features.getall()

        for name in listColumn:
            self.treeview2.heading(name, text=name)

        for valueList in all:
            self.treeview2.insert('', tk.END, values=valueList)


    def insert_stock(self):

        quantityToAddSpinbox = int(self.quantityToAdd.get())

        if self.checkbuttonStatus:
            
            newProductEntry = self.newProductEntry.get()
            priceOfNewProduct = self.priceOfNewProduct.get()
            features.add_new_items(newProductEntry, priceOfNewProduct, quantityToAddSpinbox)

        else:

            existantProductEntry = self.existantProduct.get()
            features.additems(existantProductEntry, quantityToAddSpinbox)

        # DELET TREEVIEW
        for item in self.treeview2.get_children():
            self.treeview2.delete(item)

        # RELOAD DATA STOCK
        self.load_data_stock()


    def insert_sales(self):

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

        self.quantity.set(self.getquantity)
        print("Set Quantity:", self.quantity.get())



    def callbackFunc(self, event):
        
        self.currentSelection = self.product.get()
        self.currentSelection2 = self.existantProduct.get()

    def restore_default_text(self, entry, default_text):

        # INSERT DEFAUT TEXT
        if entry.get() == "":
            entry.insert(0, default_text)

    def load_tab_login(self, tab1):

        self.widgets_frame_1 = ttk.LabelFrame(tab1, text="User Login")
        self.widgets_frame_1.pack(fill=X, side="top", padx=350)

        self.image = tk.PhotoImage(file="space-invader.png")
        self.image_label = ttk.Label(self.widgets_frame_1, image=self.image).pack()

        self.login = ttk.Entry(self.widgets_frame_1)
        self.login.insert(0, "Login")
        self.login.bind("<FocusIn>", lambda e: self.login.delete('0', 'end'))  # EVENT : DELETE LABEL IF FOCUS
        self.login.bind("<FocusOut>", lambda e: self.restore_default_text(self.login, "Login"))
        self.login.pack(pady=5)

        self.password = ttk.Entry(self.widgets_frame_1)
        self.password.insert(0, "Password")
        self.password.bind("<FocusIn>", lambda e: self.password.delete('0', 'end'))  # EVENT : DELETE LABEL IF FOCUS
        self.password.bind("<FocusOut>", lambda e: self.restore_default_text(self.password, "Password"))
        self.password.pack(pady=5)

        self.buttonSignIn = ttk.Button(self.widgets_frame_1, text='Sign in')
        self.buttonSignIn.pack(pady=5)

        self.buttonSignIn.focus_set() # INITIAL FOCUS ON BUTTON    

    def on_product_focus_out(self, event):

        if not self.product.get():
            self.product.set("Product")
            
        elif not self.existantProduct.get():
            self.product.set("Product")

    def on_frame_focus_out(self, event):
        
        self.var.set("Product")

    def load_quantity(self):
        selected_product = self.var.get()
        print("Selected Product:", selected_product)
        
        self.getquantity = features.getquantity(selected_product)
        print("Get Quantity:", self.getquantity)

        self.quantity.set(self.getquantity)
        print("Set Quantity:", self.quantity.get())


    def load_tab_add_sales(self, tab2):

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
        self.quantity = ttk.Combobox(self.widgets_frame_2, textvariable=self.varQ, values=[], state="readonly")
        self.varQ.set("Quantity")
        #self.varQ.trace('w', lambda *args: self.load_quantity())
        #self.quantity.insert(0, "Quantity")
        self.quantity.bind("<FocusIn>", lambda e: self.quantity.selection_clear())
        self.quantity.grid(row=1, column=0, sticky="ew", padx=5, pady=5)

        self.price = ttk.Entry(self.widgets_frame_2, textvariable=self.mystr, state='disabled')
        self.price.grid(row=2, column=0, sticky="ew", padx=5, pady=5)

        self.buttonAdd = ttk.Button(self.widgets_frame_2, text='Add', command=lambda: self.insert_sales())
        self.buttonAdd.grid(row=3, column=0, sticky="nsew", padx=5, pady=5)

        # TEST 06/12
        self.test = ttk.Button(self.widgets_frame_2, text='TEST', command=lambda: self.load_quantity())
        self.test.grid(row=4, column=0, sticky="nsew", padx=5, pady=5)

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
    

    def set_new_product(self):
        # checkbuttonStatus = True if self.a.get() else False
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

        else:
            self.newProductEntry.grid_remove()
            self.priceOfNewProduct.grid_remove()


    def load_tab_stock(self, tab3):

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

        self.quantityToAdd = ttk.Combobox(self.widgets_frame_3)
        self.quantityToAdd.insert(0, "Quantity")
        self.quantityToAdd.bind("<FocusIn>", lambda e: self.quantityToAdd.delete('0', 'end'))
        self.quantityToAdd.grid(row=3, column=0, sticky="ew", padx=5, pady=5)

        self.buttonAddProductStock = ttk.Button(self.widgets_frame_3, text='Add', command=lambda: self.insert_stock())
        self.buttonAddProductStock.grid(row=4, column=0, sticky="nsew", padx=5, pady=5)

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