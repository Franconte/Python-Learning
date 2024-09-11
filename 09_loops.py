    ### Loops ### 

 # While 
my_condition = 0
while my_condition < 10: 
    print (my_condition+1)   
    my_condition+=1

print('la ejecucion continua')

while my_condition < 20: 
    my_condition+=2
    if my_condition == 16: 
        print("Mi condicion es igual a 15")
        break
    
print ('Mi condicion es menor que 20')

# For 

my_list= [35, 24, 62, 40, 30, 30, 17]

for elemement in my_list: 
    print(elemement)
    
my_tuple = (35, 1.77, "Contreras", "Francisco")

for elemement in my_tuple: 
    print(elemement)
other_set = {"Lo de siempre", "Contreras", 25, "Hello W"}

for elemement in other_set: 
    print(elemement)
my_other_dict ={"Nombre":"Francisco", 
                "Apellido":"Contreras", 
                "Edad":25, 
                1:"Python"}

for elemement in my_other_dict: 
    print(elemement)
    if elemement == "Edad": 
        #Continues o go to malas practicas 
     condicion= elemement 
else: 
    print("El ciclo a finalizado")
    print(condicion)