# exo 6.13
# Multipliez chacun des nombres dans la liste par 100, réaffactez le résultat à la place de la valeur originelle puis affichez le résultat

my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.13
for item in range(len(my_list)):
    my_list[item] = my_list[item] * 100
print(my_list)
