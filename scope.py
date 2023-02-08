foo = 123 # Scope global (si la variable n'est dans rien et est dans le script princiape alors la variable est dans le scope gloabal)

def bar():
    foo = 42 # Scope local 
    print(foo)

print(foo) #123, scope global
bar() #42, scope local de la fonction bar() 
print(foo) #123, Scope global

def baz():
    print('baz' , foo) # Scope global

baz() # 123, scope global