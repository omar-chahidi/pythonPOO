#coding:utf-8

"""
    - Définition de la classe voiture
    - Création de classe Voiture avec comme 
        + atributs objet  marque + modele +couleur
        + atribut classe  numeroVoiture
    - Instantiation de classe 
        + PEUGEOT - 308    - BLANC
        + RENAULT - SCENIC - NOIRE

    exp : classe = Voiture
            atributs d'objet  : cMarque, cModele et cCouleur 
            atribut de classe : numeroVoiture
"""

class Voiture:
    # Atribut de classe
    numeroVoiture = 0
    # constructeur
    def __init__(self, cMarque, cModele, cCouleur):
        self.marque = cMarque  # atribut d'objet lui même 
        self.modele = cModele
        self.couleur = cCouleur
        Voiture.numeroVoiture +=1

print("Lancement du programme ...")

v1 = Voiture("PEUGEOT", "308", "BLANC")
print("La voiture {} est {} - {} - {}".format(Voiture.numeroVoiture, v1.marque, v1.modele, v1.couleur))

v2 = Voiture("RENAULT", "SCENIC", "NOIRE")
print("La voiture {}  est {} - {} - {}".format(Voiture.numeroVoiture,v2.marque, v2.modele, v2.couleur))