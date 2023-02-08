# l'opérateur d'affectation = permet d'injecter une valeure dans une variable

my_number1 = 123
my_number2 = -42

print(my_number1)
print(my_number2)
print(type(my_number1))

# float , nombre à virugle flottante.
# integer = nombre entier

my_number3= 3.14
my_number4= -2.71
#0.0 ou 0. ou .0é
my_number5= .0

print(type(my_number3))
print(my_number4)
print(my_number5)

my_text1 = "Ceci est une chaîne de caractères"
my_text2= "Ceci est aussi une chaîne de caractères"

print(my_text1)
print(my_text2)

# bool, booléen
#(par exemple pour accepter ou nn un formulaire)

my_boolean1 = True
my_boolean2 = False
print(my_boolean1)
print (my_boolean2)
print(type(my_boolean1))

#None , valeure nulle 
#Dans les autres langages elle peut s'appeller Null ou nil

my_none = None
print(my_none)
print(type(my_none))

#string, chaine de caractères
# double quote ou simple quote c'est pareil

my_text1 = "Ceci est une chaîne de caractères"
my_text2= "Ceci est aussi une chaîne de caractères"

print(my_text1)
print(my_text2)

#\ caractère d'échappement
#\n saute une ligne 
#\r macos
#\r \n win
# Pour afficher un \ il faut faire : \\
my_text3="abc\ndef\nghi"
my_text4= "John \"foo\" Doe"
print(my_text3)
print(my_text4)
print(type(my_text4))


a=123
b=42
#Permutation de la valeure des variables
a,b=b,a
print(a,b)

#De la droite vers la gauche

a=123
b=42
c=a
a=b
b=c
print(a,b)

# variante qui ne marche qu'avec des nombres

c=a+b
a=c-a
b=c-b
print(a,b)

# Transtypage
foo="123"
foo=int(foo)
print(type(foo))

foo=123
foo=float(foo)
print(type(foo))

foo=3.14
#flota vers int permet de suppr tout ce qui se trouve derrière la virgule
foo=int(foo)
print(foo)

foo=3.14
foo=str(foo)
print(type(foo))

#Enigme

foo=2.71
#récupérer la partie entière (2)
a=int(foo)
#récupérer la partie decimal
b=(foo)-a

print(a)
print(b)

# Transtypage = type casting = conversion d'un type de données 

# 0 donne false tout les autres nombres donnent true 
my_number6 = 10
# Conversion explicite en booléen
print(bool(my_number6))

my_text5=''
print(bool(my_text5))

my_text6=''
print(bool(my_text6))


#Conversion implicite en booléen
if bool(my_text6):
    print("L'utilisateur a mit autre chose que 0")
else:
    print("L'utilisateur a mis zéro")


# Listes 

fruits=('ananas', 'banane', 'cerise')

#OPérateur d'inclusion 

result='ananas' in fruits
print(result)
result='fraise' in fruits 
print(result)

#Conversion explicite en booléen 
result = bool(fruits)
print(result)

# conversion implicite en booléen

if bool(fruits):
    print("La liste contient des éléments")
else:
    print("La liste ne contient pas d'éléments")


# Attention None ne peut être converti en int ou float
print(bool(None))

