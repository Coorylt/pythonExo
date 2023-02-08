my_text1 = """Texte
multi-ligne
abc
foo
bar
baz"""

print(my_text1)

my_text2="texte\nmulti-ligne\nabc\nfoo\nbar"

print(my_text2)

my_number1= 123
# Interpolation avec une f-string
my_text3 = f"nombre ={ my_number1}"
print(my_text3)


my_text4= f"""
Le nombre 
est 
{my_number1}
foo
"""
print(my_text4)

# Afficher des accolades dans une heredoc string 
my_text5= f"""
{{
foo
}}
{{bar}}
"""

print(my_text5)




my_number2 = 3.14
my_text6= "Le nombre PI est " +str(my_number2) + """
et le nombre d'or est 1.61"""
print(my_text6)

# Tronquer un float dans une interpolation 
# .4f veut dire 4 chiffres après la virgule 

my_number3 = 1 / 3 
my_text7= f"1 / 3 ≃ {my_number3:.4f}"
print(my_text7)


# Les interpolations acceptent les expressions

my_text8= f"1 + 1 = {1 +1}"
print(my_text8)

# L'écriture de documentation pour une fonction 

def hello(name:str) -> None:
    """Cette fonction dit bonjour à quelqu'un 

    name str indique le nom de la personne à saluer

    return NONE"""

    print(f"Salut{name}")


# Appel d'une fonction
hello(' toto')

# help(hello)--->affiche la doc d'une fonction.

my_text9 ="AAAAA Salut AAAAAAAAAAAAAAAAAAAAAA AAAAAAAAAAAAAAA AAAAAAAAAAAAAAAAAAA AAAAAAAAA AAAA AAAA Salut AA."
# Lonugueur d'une str
my_number5= len(my_text9)
print(my_number5)

#Trouver la position du texte
my_number5=my_text9.find('Salut', my_number5 + 1)
print(my_number5)


#Compte le nombre d'occurence d'une str dans une autre str
my_number6=my_text9.count('Salut')
print(my_number6)


#Remplacement non permanent
print(my_text9.replace('Salut', 'BBB'))
#Remplacement permanent (il suffit d'écraser la variable avec sa nouvelle valeur)
my_text9=my_text9.replace('Salut', 'BBB')
print(my_text9)

# Éclate une str en liste en utilisant l'espace comme caractère de séparation des élements 
my_list1=my_text9.split()
print(my_list1)
# La fonction len() peut aussi être utilisée avec des listes pour compter le nombre d'éléments
print((len)my_list1)