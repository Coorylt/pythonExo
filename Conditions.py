import random

if True:
    print("La condition est vrai")
    print("Ce code est éxecuté")

if False: 
    print("La condition est fausse")
    print("Ce code n'est pas exécuté")

conditions_vente=False

if conditions_vente:
        print("L'utilisateur a accepté les conditions de vente")     
else:
        print("L'utilisateur n'a pas accepté les conditions de vente")

if not conditions_vente:
    print("L'utilisateur n'a pas accepté les conditions de vente")
else:
    print("L'utilisateur a accepté les conditions de vente")


emails=random.randint(0, 3)

if emails ==1:
    print("Vous avez un nouveau mail")
elif emails>1:
    print(f"Vous avez {emails} nouveaux mails")
else:
    print("Vous n'avez pas de nouveaux mails")

windows_closed = bool(random.randint(0,1))
electricity_off =  bool(random.randint(0,1))
#(f'{windows_closed =}') python écrit : windows_closer=False
print(f'{windows_closed =}')
print(f'{electricity_off=}')

if windows_closed and electricity_off:
    print("Les fenêtres sont fermées")
    print ("L'éléctricité est coupée")
elif not windows_closed and electricity_off : 
    print("Les fênetres ne sont pas fermées mais l'électricité est coupée")
elif windows_closed and not electricity_off:
    print("Les fenêtres sont fermées mais l'électricité n'est pas coupée")
else:
    print("Les fenêtres ne sont pas fermées")
    print("L'éléctricité n'est pas coupée")

bank_card = random.randint(0,1)
cash = random.randint(0,1)

print(f'{bank_card = }')
print(f'{cash = }')


if bank_card or cash :
    print("on a un moyen de paiement")

    if bank_card:
        print("On a la carte bancaire")

    if cash:
        print("On a du cash")

else:
    print("On a aucun moyen de paiement")

#Opérateur and utilie pour verifié si TOUTES les conditions sont remplis 
#L'opétateur OR est utilie pour verifé si AU MOINS 1 conditions est remplis 




# Quand on mélange or et and , il faut toujours utiliser les parenthèses
ticket = bool(random.randint(0,1))
vip = bool(random.randint(0,1))
registration = bool (random.randint(0,1))

print (f'{ticket = }')
print (f'{vip = }')
print (f'{registration = }')

if (ticket or vip) and registration:
    print("Acces authorized")
else: 
    print("Acces not authorized")



product_count= random.randint(0,50)

if product_count >20:
    print("Il y'a plus de 20 articles")
    print("RAS")
elif 5 < product_count <= 20:
    print("Il y'a plus de 5 articles")
    print("Alerte approvisionnement")
elif 0 < product_count <= 5:
    print("Il y'a plus de 0 articles")
    print("Alerte rupture iminente")
else:
    print("Il n'a plus d'article")
    print("Alerte rupture")



product_count=6
# équivalent d'un encadrement python
if product_count >5 and product_count <=20:
    print("Il y'a plus de 5 articles")
    print("Il y'a 20 ou moins d'articles")
