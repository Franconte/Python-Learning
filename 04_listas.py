### Listas ### 

my_list= list()
my_other_list=[]

print(len(my_list))

my_list= [35, 24, 62, 40, 30, 30, 17]
print(len(my_list), my_list)
my_other_list=[29,1.77, "Francisco", "Contreras"]

print(type(my_other_list))
print (my_other_list[0])
print (my_other_list[1])
print (my_other_list[-1])
print (my_other_list[-4])

age, height, name, surname = my_other_list
print(name)
print(my_list + my_other_list)

my_other_list.append("Jijijaja") 
print(my_other_list)

my_other_list.insert(1,"Azul")
print(my_other_list) 

my_other_list.remove("Azul")
print(my_other_list)
 
my_list.pop()
print(my_list)
print (my_list.pop())

del my_list[2]
print(my_list)
my_list.clear()
print(my_list)
#Ejemplo de dinamismo de tipado 
my_list= "Python cambia tipado"


print(type(my_list))