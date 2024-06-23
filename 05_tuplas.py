### Tuplas ###

my_tuple = tuple()
my_tuple = (35, 1.77, "Contreras", "Francisco")
my_other_tuple= ("Pancho", "Prueba", "Se pueden realizar interacciones en las tuplas")
sum_tuple= my_tuple+my_other_tuple 
print(my_tuple)
print(my_tuple[0])
print(my_tuple[2])
#print(my_other_tuple[5]) IndexError 

print(my_tuple.count("Contreras"))
print(my_tuple.index(1.77))
"""my_tuple[1]=1.90
    my_tuple[5]=1.50
print(my_tuple [1])
""" #Las tuplas son inmutables (No permiten asignaciones)
print(sum_tuple)
print(sum_tuple[2:6])

tuple_tolist= list(sum_tuple)
print (type(tuple_tolist))

tuple_tolist[3]="Patacones"

tuple_tolist.insert(1,40)

new_tuple=tuple(tuple_tolist)

print(new_tuple)
print(type(new_tuple))
