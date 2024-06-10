### Strings ### 

my_string="Soy un string"
another_string='String con comillas dobles'

print(len(my_string))
print(len(another_string))
print(my_string+" "+another_string)
new_line_string="String con\nsalto de linea"
tab_string="\t Este es un string con tabulacion"
print(new_line_string+" "+tab_string)

# Formateo 
name, lastname, age = "Francisco", "Contreras", 25
print ("Mi nombre es {} {} y mi edad es {}".format(name, lastname, age))
print ("Mi nombre es %s %s y mi edad es %d" %(name, lastname, age))
print (f"Mi nombre es {name} {lastname} y mi edad es {age}") #Mejor format en mi opinion

#Desempaquetado de caracteres
language ="Python" 
a,b,c,d,e,f = language
print (a) 
print (b)
print (c)
print (d)
print (e)
print (f)

#Division 
nombre= input("Cual es su nombre ")
language_slice = language [1:3]
print(language_slice)

language_slice = language [0:]
print(language_slice)

language_slice = language [-2]
print(language_slice)

language_slice = language [::-3]
print(language_slice)

language_slice = language [0:6:2]
print(language_slice)

#Funciones 

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print(language.isprintable())
print(language.lower())
print(language.upper().isupper())
print(language.lower().startswith("Py"))