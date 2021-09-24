#coding:utf-8

"""
    - (0) Héritage
        + classe mère est Vehicule
        + classe fille est Voiture
        ==> voiture hérite de véhicule ou bien voiture est une sorte de véhicule
        + classe fille avion
    
    - (1) Fonctions utiles
        + isinstance(<objet>, <classe>) : vérifie qu'un objet est de la classe renseignéé. Si oui donc True si non False
        + issubclass(<classe_fille>, <classe_mer>) : vérifie qu'une classe est fille d'une autre
""" 

# Classe Mère
class Vehicule:
    # constructuer
    def __init__(self, nomVehicule, essenceVehicule):
        self.nom = nomVehicule
        self.essence = essenceVehicule

    # methode
    def seDeplacer(self):
        print("Le véhicule {} se déplace ...".format(self.nom))

# Classe Fille
class Voiture(Vehicule):
    #constructeur
    def __init__(self, nomVoiture, essenceVoiture, puissanceVoiture):
        Vehicule.__init__(self, nomVoiture, essenceVoiture)
        self.puissance = puissanceVoiture

# ----------------------------------------------------------------------------------------
# Instance de la classe
voiture1 = Voiture("Honda Civic", 40, 182)

# ----------------------------------------------------------------------------------------
# (0) test de l'héritage
voiture1.seDeplacer()
print("La puissance de la {} est de {} cheveaux avec un reservoir de {} litre".format(voiture1.nom, voiture1.puissance, voiture1.essence))

# ----------------------------------------------------------------------------------------
# (1) test fonctions utiles
# vérifie qu'un objet est de la classe renseignée avec isinstance(<objet>, <classe>)
print(isinstance(voiture1, Voiture))
if isinstance(voiture1, Voiture):
    print("voiture1 est une instance de la classe Voiture")

if isinstance(voiture1, Vehicule):
    print("voiture1 est une instance de la classe Vehicule")

# vérifie qu'une classe est fille d'une autre avec issubclass(<classe_fille>, <classe_mer>)
if issubclass(Voiture, Vehicule):
    print("La classe Voiture hérite de la classe Vehicule")