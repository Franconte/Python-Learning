### Sets ### 

my_set = set()
other_set = {}
print(type(my_set))
print(type(other_set)) #Ininicialmente es un tipo dict

other_set = {"Lo de siempre", "Contreras", 25, "Hello W"}
print(type(other_set))

print(len(other_set))

other_set.add(50) 

print(other_set)
other_set.add(50) #No añade elementos repetidos 

print(other_set)

print ("Contreras" in other_set)
print ("Panchin" in other_set) 

other_set.remove("Contreras")
print (other_set)
my_set =  {"Lo de siempre", "Contreras", 25, "Hello W"} 
my_list= list(my_set)
print(my_list) #Mala practica, no conocemos el orden del set 
 
other_set = {"Php", "Javascript", "Java"}
my_new_set= my_set.union(other_set)
print (my_new_set)
print (my_new_set.difference(my_set))