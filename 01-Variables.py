#Variables 

variableCammelcase="Variable de tipo string"
print(variableCammelcase) 

#Python promueve el snake-case 

variable_snake ="Declaracion mas convencional de una variable en Py"
variable_int ="500"
print(variable_int)
variable_bool="false"
print(variable_bool)
print (variable_snake,variableCammelcase,variable_bool)

#Prueba de funciones de python 
to_string=str(variable_int) 
print(type(to_string))

to_int=int(to_string)+50
print (type(to_int))

to_hash=hash(to_int)
print (to_hash)

print("Este es el tamaño de mi cadena de caracteres:", len(variable_snake))

#Variables en una sola linea 

firstname, secname, alias, edad, peso ="francisco", "javier", "pancho", 22, "85kg"
#p
#print("Hola, mi nombre es:", firstname +"",secname)

"""
No se recomienda hacer declaracion multiple de variables en una sola linea
No es sostenible con el tiempo X
"""
firstname= input ("What is your name? ")
age = input("How old are you? ")

#Cambiamos nuevamente de tipo 
firstname=50 
age ="Francisco"
print (firstname, age) 

addres: str   ="Direccion aleatoria"
