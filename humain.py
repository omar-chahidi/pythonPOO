#coding:utf-8

"""
    - Définition de classe
    - Création de classe
    - Instantiation de classe 

    exp : classe des êtres humain
"""
class Humain:
    # constructeur
    def __init__(self):
        #pass  # passe au suivant. elle ne fait rien cette fonction pass
        print("Création d'un Humain ...")
        self.prenom = "Omar"
        self.age    = 37


print("Lancement du programme ...")

# Instance de Humain => humain 1 = h1
h1 = Humain()
print("Vous êtes l'humain {} et votre âge est de {} ans".format(h1.prenom, h1.age))