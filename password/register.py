import crypto

# Exemple d'utilisation
id = input("Entrez votre identifiant : ")
mdp = input("Entrez votre mot de passe : ")
group=input("Entrez votre group :")
fichier_utilisateurs = "utilisateurs.txt"
sentence = id+":"+mdp+":"+group
decalage = 3  # Décalage de 3 positions
sentence_crypted = crypto.cesar(sentence, decalage)
crypto.ajouter_utilisateur_crypte(sentence_crypted,fichier_utilisateurs)