### Dictionaries ### 

my_dict= dict()
my_other_dict = {  }

print(type(my_dict))
print (type(my_other_dict))

my_other_dict ={"Nombre":"Francisco", 
                "Apellido":"Contreras", 
                "Edad":25, 
                1:"Python"}
my_dict= {  
        "Nombre":"Francisco", 
        "Apellido":"Contreras", 
        "Edad":25, 
        "Lenguajes":{"Python", "Swift", "Perl"}, 
         1:1.80}

print(my_dict["Lenguajes"])
print(my_other_dict)
print(len(my_dict ))

my_dict["Nombre"]="Pancho" 
print(my_dict["Nombre"])  

my_dict["Calle"]="Calle pancho" #1 Forma de asignar nuevo valor 
print(my_dict)

del my_dict["Calle"] #Eliminar un valor determinado con la variable global del 
print ("Contreras" in my_dict) #False
print ("Apellido" in my_dict) #True toma la key 

my_list=["nombre",1,"Javier"]
my_new_dict=my_dict.fromkeys(("Nombre","Apellido","Perro hpta"),20)
my_dict_list=dict.fromkeys(my_list)
print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())  
print(my_new_dict)
print(my_dict_list)


print(list(my_new_dict))
print(tuple(my_new_dict))
print(set(my_new_dict))
