import login_library.crypto as crypt

"""
@AUTHOR : Julian DALPAN
@VERSION : 1.0.0

"""

decalage=3
# Fonction pour vérifier les identifiants et mots de passe
def login_identify(identifiant, mot_de_passe, fichier_utilisateurs,app,tab2,tab3,tabControl):

    with open(fichier_utilisateurs, 'r') as fichier:
        lignes = fichier.readlines()
        for ligne in lignes:
            # Divise la ligne en identifiant et mot de passe
            utilisateur, mdp = ligne.strip().split(':')
            if utilisateur == crypt.cesar(identifiant,decalage) and mdp== crypt.cesar(mot_de_passe,decalage):

                tabControl.add(tab2, text='Sales')
                tabControl.add(tab3, text='Stock')
                treeview = app.load_tab_add_sales(tab2)
                app.load_tab_stock(tab3)
                app.load_data_sales(treeview)
                return True
            
    print("Bad password")
    acces=False

    return False