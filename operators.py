import random
import math

# = affectation
foo=123
# + addition
foo=123+42
foo=foo+42 #--> calcul recursif 
# += opérateur d'incrémentation 
foo+=42
# - soustraction
foo=123-42
foo=foo-42
# -= opérateur de décrémentation
foo-=42
# / division
foo=123/42
# // division entière
foo=123//42
# % modulo
foo=4%3
foo=random.randint(1,100) 
print(foo%2)
# * multiplication
foo=123*42
# ** puissance
foo=2**2
foo=2**3
foo=2**4
foo=2**5
foo=2**6
# sqrt() racine carré
foo=math.sqrt(4)
foo=4 **0.5
foo=4**(1/2)
print(foo)
#racine cubique
foo=8**(1/3)
print(foo)

# les opérateurs de comparaison

# L'égalité ==
# A ne pas confondre avec l'affectation =
# A ne pas confondre avec l'identitée (javascript) --> ===
result= 1 ==1
print(result)

# Les grandeurs 

#plus petit ou égal à et plus grand que 
# A ne pas confondre avec => js 
result = 123<42
print(result)

# L' inégalité (ou différence)
result=123 !=42

# Les encadrements
# < > <= >=

my_number= random.randint(0,100)
print(my_number)
result= 0 <= my_number < 50
print(result)
result= 50 < my_number <= 100
print(result)

# Opérateur logique 
# Opérateur and 
result =True and False #False
print(result)
result = False and True #False
print(result)
result= True and True #True
print(result)
result= False and False #False
print(result)

a=random.randint(0,1)
b=random.randint(0,1)
result= a and b
print(a , b)
print(result)


# utilisation un peu spéciales des comparaisons de grandeur 
result="abc" > "bcd"
print(result)


# Opérateur or 

result =True or False #False
print(result)
result = False or True #False
print(result)
result= True or True #True
print(result)
result= False or False #False
print(result)


#On peut utiliser d'autres type de données que l'on converti en booléen ave les opérateurs booléens
a=random.randint(0,1)
b=random.randint(0,1)
result = bool(a) and bool(b)

print()

fruits=['abricot','cerise','baie']
result='ananas' in fruits
print(result)
result='cerise' in fruits
print(result)