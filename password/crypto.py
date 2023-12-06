def cesar(sentence, decalage):
    sentence_crypted = ""
    
    for character in sentence:
        if character.isalpha():  # Vérifie si la character est alphabétique
            minuscule = character.islower()
            character = character.lower()  # Convertit en minuscule pour le traitement
            character_decalee = chr(((ord(character) - ord('a') + decalage) % 26) + ord('a'))
            if minuscule:
                sentence_crypted += character_decalee
            else:
                sentence_crypted += character_decalee.upper()
        else:
            sentence_crypted += character  # Conserve les caractères non alphabétiques

    return sentence_crypted

def ajouter_utilisateur_crypte(sentence_crypted, fichier_utilisateurs):
    with open(fichier_utilisateurs, 'a') as fichier:
        fichier.write(sentence_crypted + '\n')


