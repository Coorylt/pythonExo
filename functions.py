from collections.abc import Callable
import random
import my_library
from my_library import randint_list


def addition(a:float,b:float) -> float :
    """
    Cette fonction permet d'additioner deux nombres
    a -- float le premier nombre à additionner
    b -- float le deuxième nombre à additionne
    return -- float le résultat de l'addition
    """
    result = a + b 

    return result  

result = addition(123,42)
print(result)

my_number1 = 123 
my_number2 = 42 
result=addition(my_number1, my_number2)
print(result)


def calculer(calcul1:Callable, calcul2:Callable, a:float, b:float, c:float) -> float :
    result = calcul1(a,b)
    result = calcul2 (result, c)

    return result

result = calculer(addition, addition,123,42,3.14)
print(result)

# Le code "from my_library import randin_list" permet de ne pas préciser le nom de la librairie
# le code "import my_library" oblige à préciser le nom de la librairie devant le nom de la fonction.


my_list = my_library.randint_list(0,100,10)
print(my_list)


result = addition(123,42)
print(result)


# écrire une fonction qui accepte en paramètre une liste et qui renvoie la moyenne des nombres de la liste 

def my_average(numbers:list) -> float:
    
    my_sum = 0

    for number in numbers:
        my_sum += number

    result = my_sum / len(numbers)
        
    return result