

import login_library.crypto as crypt
decalage=3
# Fonction pour vérifier les identifiants et mots de passe
def login_identify(identifiant, mot_de_passe, fichier_utilisateurs):
    with open(fichier_utilisateurs, 'r') as fichier:
        lignes = fichier.readlines()
        for ligne in lignes:
            # Divise la ligne en identifiant et mot de passe
            utilisateur, mdp = ligne.strip().split(':')
            if utilisateur == crypt.cesar(identifiant,decalage) and mdp== crypt.cesar(mot_de_passe,decalage):
                print("loginet password ok!")
                return True
    print("pas bon jack")
    return False
##
### Fichier contenant les identifiants et mots de passe
##fichier_utilisateurs = 'utilisateurs.txt'  # Assurez-vous de créer ce fichier
##
### Saisie de l'identifiant et du mot de passe depuis la console
##identifiant_saisi = input("Entrez votre identifiant : ")
##mot_de_passe_saisi = input("Entrez votre mot de passe : ")
##
### Vérifie les identifiants et mots de passe
##if login(identifiant_saisi, mot_de_passe_saisi, fichier_utilisateurs):
##    print("OK")
##else:
##    print("Identifiant ou mot de passe incorrect")
