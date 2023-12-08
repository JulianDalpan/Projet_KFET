import database
import datetime
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle,Paragraph,Image
from reportlab.lib.styles import getSampleStyleSheet

#Chemin du pdf
PDF_path="SALES_"+datetime.datetime.now().strftime('%Y_%m_%d')+".pdf"
image_path="logo-esirem.jpg"

#Fais +1 a la quantité d'un item donné
def additems(name,quantity):
    qu=getquantity(name)
    purchased_price=database.getpurchased_price(name)
    database.addItems(name,getprice(name),quantity+int(qu),purchased_price[0]['purchasedprice'])


#Fais -1 a la quantité d'un item donné
def subbitems(name,quantity):
    qu=getquantity(name)
    purchased_price=database.getpurchased_price(name)
    database.addItems(name,getprice(name),int(qu)-quantity,purchased_price[0]['purchasedprice'])

#Ajoute un nouvelle item a la base de données
def add_new_items(name,price,quantity,purchased_price):
    database.addItems(name,price,quantity,purchased_price)

#Recupere la quantité d'un item donné
def getquantity(name):
    return database.getStock(name)[0]['quantity']

#Recupere le prix d'un item donné
def getprice(name):
    if database.getPrice(name)==[]:
        return database.getPrice(name)
    else:
        return database.getPrice(name)[0]['price']
    
#Ajoute un vente dans la base de données
def addsales(product,quantity):
    subbitems(product,quantity)
    database.addSales(product,getprice(product)*quantity,quantity,(datetime.datetime.now()).strftime('%Y-%m-%d %H:%M:%S'),1) #1 corresponding to the team

#Recupere toute les information de la table ITEM de la base de données
def getall():
    product=[]
    for elem in database.getAll():
        product.append([elem['name'],elem['price'],elem['quantity']])
    return product

#Recupere toute les vente effectuée
def getallsale():
    product=[]
    for elem in database.getALLSale():
        product.append([elem['product'],elem['price'],elem['quantity'],elem['time'],elem['team']])
    return product

#Recupere le derniere vente effectuée
def getlastsale():
    product=[]
    for elem in database.getLastSale():
        product.append([elem['product'],elem['price'],elem['quantity'],elem['time'],elem['team']])
    return product

#Recupere tout les items de la base de données
def getallitem():
    product=[]
    for elem in database.getAllItem():
        product.append(elem['name'])
    return product

#Genere un PDf a partir des vente effectuer le jours meme en classant par produit et en donnant la quantité total ainsi que le benefice total
def generate_sale_pdf():
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
    return database.getItemSale(name)

#Recupere la quantité total de vente d'un item donné
def get_total(name):
    tab=get_item_sale(name)
    total_quantity=0

    for elem in tab:
        total_quantity=int(elem['quantity'])+total_quantity

    return(total_quantity)

def delet_item(name):
    database.DeleteItem(name)


def listColumnSales():
    column=('Product','Price','Quantity','Time')
    return column

def listColumnStock():
    column=('Product','Price','Quantity','Update')
    return column
