import database
import datetime
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle,Paragraph,Image
from reportlab.lib.styles import getSampleStyleSheet

#Chemin du pdf
PDF_path="Exported_Pdf/SALES_"+datetime.datetime.now().strftime('%Y_%m_%d')+".pdf"
image_path="img/logo-esirem.jpg"


def additems(name,quantity):
    """
    Add a specified quantity of items to the inventory.

    Parameters:
    - name (str): The name of the item.
    - quantity (int): The quantity of items to be added.

    Returns:
    None

    Example:
    >>> additems("Coca-Cola", 10)
    # Assuming the initial quantity of apples is 5 and purchased price is $1.50
    # The inventory for apples will be updated to 15 (5 + 10) with the same purchased price.
    """
    qu=getquantity(name)
    purchased_price=database.getpurchased_price(name)
    database.addItems(name,getprice(name),quantity+int(qu),purchased_price[0]['purchasedprice'])



def subbitems(name,quantity):
    """
    Subtract a specified quantity of items from the inventory.

    Parameters:
    - name (str): The name of the item.
    - quantity (int): The quantity of items to be subtracted.

    Returns:
    None

    Example:
    >>> subbitems("Coca-Cola", 5)
    # Assuming the initial quantity of bananas is 10 and purchased price is $2.00
    # The inventory for bananas will be updated to 5 (10 - 5) with the same purchased price.
    """
    qu=getquantity(name)
    purchased_price=database.getpurchased_price(name)
    database.addItems(name,getprice(name),int(qu)-quantity,purchased_price[0]['purchasedprice'])


def add_new_items(name,price,quantity,purchased_price):
    """
    Add new items to the inventory with the specified details.

    Parameters:
    - name (str): The name of the new item.
    - price (float): The price of the new item.
    - quantity (int): The initial quantity of the new item.
    - purchased_price (float): The purchased price of the new item.

    Returns:
    None

    Example:
    >>> add_new_items("orange", 1.25, 20, 1.00)
    # Adds a new item 'orange' to the inventory with a price of $1.25,
    # an initial quantity of 20, and a purchased price of $1.00.
    """
    database.addItems(name,price,quantity,purchased_price)


def getquantity(name):
    """
    Get the current quantity of a specific item from the inventory.

    Parameters:
    - name (str): The name of the item.

    Returns:
    int: The current quantity of the specified item in the inventory.

    Example:
    >>> getquantity("apple")
    # Assuming the current quantity of apples in the inventory is 15.
    # Returns 15.
    """
    return database.getStock(name)[0]['quantity']


def getprice(name):
    """
    Get the current price of a specific item from the inventory.

    Parameters:
    - name (str): The name of the item.

    Returns:
    float or list: If the item is found in the inventory, returns the current price of the item.
                  If the item is not found, returns an empty list.

    Example:
    >>> getprice("banana")
    # Assuming the current price of bananas in the inventory is $1.50.
    # Returns 1.50.

    >>> getprice("watermelon")
    # Assuming there is no entry for watermelon in the inventory.
    # Returns [].
    """
    if database.getPrice(name)==[]:
        return database.getPrice(name)
    else:
        return database.getPrice(name)[0]['price']
    

def addsales(product,quantity):
    """
    Record a sales transaction for a specific product.

    Parameters:
    - product (str): The name of the product being sold.
    - quantity (int): The quantity of the product being sold.

    Returns:
    None

    Example:
    >>> addsales("apple", 3)
    # Assuming the current quantity of apples is 10 and the price is $1.00.
    # After the sales, the quantity of apples will be updated to 7 (10 - 3).
    # A sales entry will be added with a total amount of $3.00 (3 * $1.00),
    # a quantity of 3, and the current timestamp for the team with ID 1.
    """

    subbitems(product,quantity)
    database.addSales(product,getprice(product)*quantity,quantity,(datetime.datetime.now()).strftime('%Y-%m-%d %H:%M:%S'),1) #1 corresponding to the team

#Recupere toute les information de la table ITEM de la base de données
def getall():
    """
    Retrieve information for all products in the inventory.

    Returns:
    list: A list containing information for each product in the inventory.
          Each element in the list is a sublist with the format [name, price, quantity].

    Example:
    >>> getall()
    # Assuming the inventory contains the following entries:
    # [{'name': 'apple', 'price': 1.00, 'quantity': 10},
    #  {'name': 'banana', 'price': 1.50, 'quantity': 15},
    #  {'name': 'orange', 'price': 1.25, 'quantity': 20}]
    # Returns [['apple', 1.00, 10], ['banana', 1.50, 15], ['orange', 1.25, 20]].
    """
    product=[]
    for elem in database.getAll():
        product.append([elem['name'],elem['price'],elem['quantity'],elem['purchasedprice']])
    return product

#Recupere toute les vente effectuée
def getallsale():
    """
    Retrieve information for all sales transactions.

    Returns:
    list: A list containing information for each sales transaction.
          Each element in the list is a sublist with the format [product, price, quantity, time, team].

    Example:
    >>> getallsale()
    # Assuming the sales transactions log contains the following entries:
    # [{'product': 'apple', 'price': 3.00, 'quantity': 3, 'time': '2023-12-30 15:30:00', 'team': 1},
    #  {'product': 'banana', 'price': 6.00, 'quantity': 4, 'time': '2023-12-30 16:45:00', 'team': 1},
    #  {'product': 'orange', 'price': 2.50, 'quantity': 2, 'time': '2023-12-30 18:00:00', 'team': 1}]
    # Returns [['apple', 3.00, 3, '2023-12-30 15:30:00', 1],
    #          ['banana', 6.00, 4, '2023-12-30 16:45:00', 1],
    #          ['orange', 2.50, 2, '2023-12-30 18:00:00', 1]].
    """
    product=[]
    for elem in database.getALLSale():
        product.append([elem['product'],elem['price'],elem['quantity'],elem['time'],elem['team']])
    return product

#Recupere le derniere vente effectuée
def getlastsale():
    """
    Retrieve information for the most recent sales transaction.

    Returns:
    list: A list containing information for the most recent sales transaction.
          The list is a sublist with the format [product, price, quantity, time, team].

    Example:
    >>> getlastsale()
    # Assuming the most recent sales transaction log entry is:
    # {'product': 'banana', 'price': 6.00, 'quantity': 4, 'time': '2023-12-30 16:45:00', 'team': 1}
    # Returns [['banana', 6.00, 4, '2023-12-30 16:45:00', 1]].
    """
    product=[]
    for elem in database.getLastSale():
        product.append([elem['product'],elem['price'],elem['quantity'],elem['time']])
    return product[0]

#Recupere tout les items de la base de données
def getallitem():
    """
    Retrieve the names of all items in the inventory.

    Returns:
    list: A list containing the names of all items in the inventory.

    Example:
    >>> getallitem()
    # Assuming the inventory contains the following entries:
    # [{'name': 'apple', 'price': 1.00, 'quantity': 10},
    #  {'name': 'banana', 'price': 1.50, 'quantity': 15},
    #  {'name': 'orange', 'price': 1.25, 'quantity': 20}]
    # Returns ['apple', 'banana', 'orange'].
    """
    product=[]
    for elem in database.getAllItem():
        product.append(elem['name'])
    return product

#Genere un PDf a partir des vente effectuer le jours meme en classant par produit et en donnant la quantité total ainsi que le benefice total
def generate_sale_pdf():
    """
    Generate a sales report in a PDF format.

    Reads the sales information for each product, calculates total benefits, and creates a PDF report.

    Requires:
    - The function relies on various helper functions like 'getallitem()', 'get_total()', 'getprice()', etc.
    - The global variable 'image_path' needs to contain the path to an image for the report.

    Returns:
    None

    Example:
    >>> generate_sale_pdf()
    # Generates a PDF file containing a sales report with product details, total earnings, and benefits.
    """
    global image_path
    document = SimpleDocTemplate(PDF_path, pagesize=letter)

    # Entete du tableau dans le PDF
    data = [["Product", "Total (€)", "Quantity","Benefits"]]
    
    #Rempli le tableau avec les different produit ainsi que leur prix et leur quantité vendu dans la journée
    item=getallitem()
    Total_benefit=0
    for elem in item:
        Total=round(int(get_total(elem))*float(getprice(elem)),2)
        benefits=round(Total-(float(database.getpurchased_price(elem)[0]['purchasedprice'])*int(get_total(elem))),2)
        Total_benefit=benefits+Total_benefit
        data.append([elem,
                     Total,
                     get_total(elem),
                     benefits
                     ])
    data.append(["","","","Total benefit="+str(Total_benefit)])

    # Crée le tableau du PDf
    table = Table(data)

    # Ajoute un style au tableau
    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                       ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                       ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                       ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                       ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                       ('BACKGROUND', (0, 1), (-1, -1), colors.white),
                       ('GRID', (0, 0), (-1, -1), 1, colors.black)])

    table.setStyle(style)
    title = Paragraph("<u>SALES REPORT {}</u>".format(datetime.datetime.now().strftime('%Y %m %d')), getSampleStyleSheet()['Title'])
    space= Paragraph("<u> </u>", getSampleStyleSheet()['Title'])
    image = Image(image_path)  # Ajustez la largeur et la hauteur selon vos besoins
    
    # Liste d'elements' à ajouter au PDF
    elements = [image,space,space,title,space,table]
    # Construit le PDF
    document.build(elements)

#Recupere toute le vente pour un item données
def get_item_sale(name):
    """
    Retrieve sales information for a specific item.

    Parameters:
    - name (str): The name of the item.

    Returns:
    list: A list containing sales information for the specified item.
          Each element in the list represents a sales entry with details such as price, quantity, time, and team.

    Example:
    >>> get_item_sale("apple")
    # Assuming there are sales entries for apples with the following format:
    # [{'price': 3.00, 'quantity': 3, 'time': '2023-12-30 15:30:00', 'team': 1},
    #  {'price': 1.50, 'quantity': 2, 'time': '2023-12-30 16:00:00', 'team': 2}]
    # Returns [{'price': 3.00, 'quantity': 3, 'time': '2023-12-30 15:30:00', 'team': 1},
    #          {'price': 1.50, 'quantity': 2, 'time': '2023-12-30 16:00:00', 'team': 2}].
    """
    return database.getItemSale(name)

#Recupere la quantité total de vente d'un item donné
def get_total(name):
    """
    Calculate the total quantity sold for a specific item.

    Parameters:
    - name (str): The name of the item.

    Returns:
    int: The total quantity sold for the specified item.

    Example:
    >>> get_total("banana")
    # Assuming there are sales entries for bananas with the following format:
    # [{'quantity': 4, 'time': '2023-12-30 16:45:00', 'team': 1},
    #  {'quantity': 2, 'time': '2023-12-30 17:30:00', 'team': 2}]
    # Returns 6 (4 + 2).
    """
    tab=get_item_sale(name)
    total_quantity=0

    for elem in tab:
        total_quantity=int(elem['quantity'])+total_quantity

    return(total_quantity)

def delet_item(name):
    """
    Delete a specific item from the inventory.

    Parameters:
    - name (str): The name of the item to be deleted.

    Returns:
    None

    Example:
    >>> delet_item("orange")
    # Deletes the item with the name 'orange' from the inventory.
    """
    database.DeleteItem(name)


def listColumnSales():
    """
    Get the list of columns for displaying sales information.

    Returns:
    tuple: A tuple containing column names for displaying sales information.
           The columns are in the order: ('Product', 'Price', 'Quantity', 'Time').

    Example:
    >>> listColumnSales()
    # Returns ('Product', 'Price', 'Quantity', 'Time').
    """
    column=('Product','Price','Quantity','Time')
    return column

def listColumnStock():
    """
    Get the list of columns for displaying stock information.

    Returns:
    tuple: A tuple containing column names for displaying stock information.
           The columns are in the order: ('Product', 'Price', 'Quantity', 'Update').

    Example:
    >>> listColumnStock()
    # Returns ('Product', 'Price', 'Quantity', 'Update').
    """
    column=('Product','Price','Quantity','Update')
    return column
