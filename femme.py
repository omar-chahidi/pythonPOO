#coding:utf-8

"""
    + Propriétés d'encapsulation <=> contrôler l'accé au attribut d'une classe avec des getter et des setter
    + propriété : manière de manipuler et contrôler des attributs => principe d'encapsulation
    + encapsulation d'une propriété avec des <getter>  <setter> <deleter>  <helper>
    + exp : on veut contrôler l'age d'une femme c'est à dire 
            - changer l'age
            - modifier
            - mettre des condition    
    + getter et setter s'appellent aussi des accesseurs / mutateurs  
"""

# Debut de classe 
class Femme:

    # -----------------------------------------------------
    # (0) constructeur
    def __init__(self, nom, age):
        print("Définition d'une femme ...")
        self.nom = nom
        self._age = age # controler l'age <=> principe d'encapsulation
    
    # -----------------------------------------------------
    # Encapsulation
    def _getage(self):
        #return self._age
        if self._age <=1:
            return "{} {}".format(self._age, "an")
        else:
            return "{} {}".format(self._age, "ans")

    def _setage(self, nouveauAge):
        if nouveauAge < 0:
            self._age = 0
        else:
            self._age = nouveauAge
    # définir une variable "age" pour l'encapsulation 
    age = property(_getage, _setage)

    #

# Fin de classe 

# ----------------------------------------------------------------------------------------
# Instance de la classe
f1 = Femme("Brigitte", 55)

# ----------------------------------------------------------------------------------------
# (0) test de constructeur
print("age de {} est {} ans".format(f1.nom, f1._age))

# ----------------------------------------------------------------------------------------
# (0) test l'encapsulation
# (0-1) test l'encapsulation de setter
f1.age = -5
# (0-1) test l'encapsulation de getter
print("Nouveau age de {} est {}".format(f1.nom, f1.age))
f1.age = 15
print("Nouveau age de {} est {}".format(f1.nom, f1.age))
