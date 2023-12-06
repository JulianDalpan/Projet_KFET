import database
import features as features


features.add_new_items('Coca-Cola',0.9,100,0.3)
#features.additems('Fanta',300)
print(features.getquantity('Coca-Cola'))
features.addsales('Coca-Cola',3)

print("result"+str(database.getStock('Coca-Cola')[0]['quantity']))
features.generate_sale_pdf()
