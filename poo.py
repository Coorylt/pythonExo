# POO programmation orienté objet

class Voiture:
    # Constructeur
    # En JS, on utilise "this" au lieu de "self"
    # le mot clé self désign l'instance en cours d'utilisation
    def __init__(self):
        self._passagers = 0
        self._vitesse = 0


# Méthode de type getter 
# C'est une fonction qui permet de lire une variable 
def getPassagers(self):
    return self._passagers

# Méthode type setter
# C'est une fonction qui permet de modifié une variable 
def setPassagers(self,passagers):
    if passagers is int and passagers >=0 and passagers <=4 :
         self._passagers = passagers


def getVitesse(self):
    return(self._vitesse)

def setVitesse(self,vitesse):
    if (type (vitesse) is int or type (vitesse) is float) and vitesse >=-10 and vitesse <=240:
        self._vitesse = vitesse

# v est une instance de la classe Voiture
# v est un objet de la classe voiture 
v1 = Voiture() # 
print(v1.passagers)
print(v1.vitesse)
v1.passagers = 3 
v1.vitesse = 50
print (v1.passagers)
print (v1.vitesse)

print( )

v2 = Voiture()
print(v2.passagers)
print(v2.vitesse)