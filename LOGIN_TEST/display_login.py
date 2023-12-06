import tkinter as tk
from tkinter import messagebox
import crypto
decalage=3
fichier_utilisateurs = 'utilisateurs.txt' 

def login_check(identifiant, mot_de_passe,groupes, fichier_utilisateurs):
    with open(fichier_utilisateurs, 'r') as fichier:
        lignes = fichier.readlines()
        for ligne in lignes:
            # Divise la ligne en identifiant et mot de passe
            utilisateur, mdp ,group= ligne.strip().split(':')
            if utilisateur == crypto.cesar(identifiant,decalage) and mdp== crypto.cesar(mot_de_passe,decalage) and group==crypto.cesar(groupes,decalage):
                return True
    return False

def valider():
    # Récupérer les valeurs des champs
    login= entry_login.get()
    password = entry_password.get()
    group=entry_group.get()
    # Vérifier si le login et le mot de passe sont corrects (à adapter selon vos besoins)
    if login_check(login,password,group,fichier_utilisateurs):
        messagebox.showinfo("Validation", "Login et mot de passe valides")
    else:
        messagebox.showerror("Erreur", "Login, mot de passe ou group incorrect")

# Créer la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Authentification")

# Créer les widgets
label_login = tk.Label(fenetre, text="Login :")
label_password = tk.Label(fenetre, text="Mot de passe :")
label_group = tk.Label(fenetre,text="Group :")
entry_login = tk.Entry(fenetre)
entry_password = tk.Entry(fenetre, show="*")
entry_group = tk.Entry(fenetre)  # Utilise le mode 'show' pour masquer le mot de passe

bouton_valider = tk.Button(fenetre, text="Valider", command=valider)

# Organiser les widgets dans la fenêtre
label_login.grid(row=0, column=0, padx=10, pady=10)
entry_login.grid(row=0, column=1, padx=10, pady=10)
label_password.grid(row=1, column=0, padx=10, pady=10)
entry_password.grid(row=1, column=1, padx=10, pady=10)
label_group.grid(row=2, column=0, padx=10, pady=10)
entry_group.grid(row=2, column=1, padx=10, pady=10)
bouton_valider.grid(row=3, column=0, columnspan=2, pady=10)

# Lancer la boucle principale
fenetre.mainloop()
