# Pourquoi utiliser certaines fonctions et pas d'autres 

path = "/home/foo/"
filename = "document.txt"


# On vérifie si le dernier caractère de path est un slash '/' ou non
# La fonction str.endswith('/') permet de faire le meme test que if path[-1] == '/':
if path.endswith('/'):   
    # Le dernier caractère est un slash
 file_path = path + filename 
else:
    # Le dernier caractère n'est pas un slash
    file_path = path +'/'+ filename


print(file_path)

# Q : Pourquoi est-ce que parfait on appelle une fonction dans une autre fonction ?
# R= Deux critères : 1 --> La lisibilité du code 2 --> Optimisation du code (est-ce que j'ai besoin de réutiliser le résultat d'une fonction ?)
lenght = len(file_path)
print(lenght)

#Les deux étapes en 1 seule 
print(len(file_path))


# Q: l'exo avec les nombres pair 


a = 58
b = 2 
print(divmod(a,b))


#Est-ce que a est divisible par b ? (autrement dis, est-ce que a est un nombre pair?)
print(a % b == 0)

#Est-ce que a est NON divisible par b ? 
print(a %2 != 0)


# q: Utilisation de len(list) dans range()?
# Même base que la boucle for avec range()
# Note : len(users) == 3 

users = ["aaaa","caca@gmail.com","teddy"]

for i in range(0,len(users)):
    print(i,users[i])



