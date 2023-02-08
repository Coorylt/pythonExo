fruits = ('anansa','banane','cerise')
print(fruits)

# Accès en lecture au 0ème élément de la liste 

print(fruits[0])

my_fruit = fruits[0]
print(my_fruit)

# Accès en écriture au 0ème éléments de la liste

#fruits[0]='abricot'
#print(fruits)
#print(fruits[0])

my_count=len(fruits)

index=0
print(fruits[index])

index +=1 
if index < my_count:
    print(f'{index=}')
    print(fruits[index])


my_text9='A'

# Accès en écriture interdit 
# my_text9[0]='A'

# Accès en lecture du 0ème au 10ème caractères de la str 
print(my_text9[0:10])

# Accès en lecture du 10ème caractère à la fin de la str 
print(my_text9[10:1])

# Accès en lecture par la fin de la str
print(my_text9[::-1])

print(my_text9[::2])




# Ajouter un élément 
fruits = ['anans','banane','cerise']
fruits.append('datte')
print(fruits)
# Supprimer un élément 


# Insérer un élément 