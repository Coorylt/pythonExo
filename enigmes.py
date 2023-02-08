# 2. Entiers conséctutifs
# 198, 199, 200, 201 et 202 sont des entiers consécutifs dont la somme est égale à 1000.
# Trouvez d'autres entiers conséctufis dont la somme vaut 1000



somme = 0 
nombres = []

for i in range (1,500):
    nombres.append(i)
    somme = sum(nombres)


    while somme > 1000:
        nombres.pop(0)
        somme = sum(nombres)

    if somme == 1000:
        print(nombres)
