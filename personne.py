#coding:utf-8

"""
    - Création de la classe Personne avec :
        + attributs nom et age
        + methode parler / change de ville / afficher un message

    - (1) Méthode           : fonction sur une instance c'est à dire fonction d'objet
    - (2) Méthode de classe : fonction sur une classe
                                lorsqu'on donne un attribut à la classe avec une initialisation et ensuite on veux le changer
                                exp : on va créer des personne OBJETS qui habite à Morsange sur orge ensuite on veux créer d'autres 
                                        OBJET qui habite à paris.
                                        donc l'atrribut  lieuHabitation va changer 
    - (3) Méthode statique  : fonction indépendante mais "lié" à une classe 
                                c'est une méthode utilitaire on l'appelle sans créer un objet de la classe 
"""

class Personne:

    # attribut de la classe pour l'utiliser dans (2) méthode de classe
    lieuHabitation = "Morsang-Sur-Orge"

    # (0) constricteur de la classe
    def __init__(self, nom, age):
        self.nom = nom 
        self.age = age
    

    #...................................
    # (1) Méthode tandard
    def parler(self, message):
        print("{} a dit : {}".format(self.nom, message))


    #...................................
    # (2) Méthode de classe
    def changerVille(cls, nouvelleVille):
        Personne.lieuHabitation = nouvelleVille

    # on va définir une variable de la methode classe avec le même nom 
    changerVille = classmethod(changerVille)


    #...................................
    # (3) Méthode statique
    def afficherUnMessage():
        print("Une personne est un ëtre humain")
    afficherUnMessage = staticmethod(afficherUnMessage)

# Fin de classe Personne

#------------------------------------------------------------------
# Instance d'objet
p1 = Personne("Omar", 37)

#------------------------------------------------------------------
# (1) tester méthode standard 
p1.parler("Bonjour à tous !")
p1.parler("J'espère  que vous allez bien :-) ")

#------------------------------------------------------------------
# (2) tester méthode classe
print("La ville actuelle de toutes les personnes : {}".format(Personne.lieuHabitation))
Personne.changerVille("Paris")
print("La nouvelle ville à partir de maintenant de toutes les personnes : {}".format(Personne.lieuHabitation)) 

#------------------------------------------------------------------
# (3) tester méthode statique
Personne.afficherUnMessage()

