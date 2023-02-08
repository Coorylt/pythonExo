# While == tant que 

while False:
    print("ce message ne sera pas affiché")

    while True :
         print('ce message sera affiché en boucle')

counter = 10 

while counter :
        print(f"{counter = }")
        counter -= 1
        # même chose 
        # counter = counter - 1 `

print()

counter = 0


#Le nombre de boucle = valeur limite - la premère valeur du compteur 
while counter <=10:
    print(f"{counter = }")
    counter += 2
    #même chose
    # counter = counter + 2 


for counter in range (0,10):
    print(f'{counter = }')



for counter in range(10,0,-1):
    print(f'{ counter = }')

print()

#Le troisième paramètre de range permet de spécifier l'incrément 
# Exemple avec un incrément de 2 (au lieu de 1)
for counter in range (0,10,2):
    print(f'{counter = }')






fruits=['abricot', 'baie','cerise']

#Bouccle de type for each == pour chaque (boucle la plus simple)
for i, foo in enumerate(fruits):
   print(f'{i +1}=:{foo}')






# reversed() renvoie un itérateur économe en mémoire 
print(reversed(fruits))
# [::1] renvoie une liste dont la taille est égale à la liste originale (peut ne pas être économe en mémoire)
print(fruits[::-1])


for foo in reversed(fruits):
    print(foo)

for foo in fruits[::-1]:
    print(foo)



my_list = [123,2,42,3,14,56]

my_number=2
counter=0

for item in my_list: 
    if item==my_number:
        counter+=1

print(f'{counter = }')


accumulateur = 0 

for item in my_list:
    accumulateur += item   

print(f'{accumulateur = }')


#(utile pr interchanger des élements 2 a2 )




fruits=['abricot', 'baie','cerise']

for i in range (0,len(fruits),2):
    print(fruits[i])


#tableau

my_array=[
    ['a', 'c'],
    ['b','d']
]

#Boucle for dans une boucle for (pour tableau)
# len(my_array) me donne le nombre de lignes
for i in range(0,len(my_array)):
    #len (my_array[0]) me donne le nombre de cologne
    for j in range (0,len(my_array[0])):
        print(i,j, my_array[i][j])
#Pour aborder à partir des colones il faut intervertir le I et le J 