# MODULO Un modulo se puede definir que es lo mismo a una biblioteca de código.
#  Es decir es un archivo que contiene un conjunto de funciones que se pueden aplicar.

# Como crear un Módulo?
# Para crear un módulo debemos escribir el nombre del archivo + la extensión de
#  python que es .py ejemplo name.py
# Escribimos el código que vamos a utilizar en el archivo que acabamos de nombrar.
# Abrimos el archivo con el cual vamos a trabajar y declaramos el modulo que le dimos
#  el nombre por ejemplo con la extensión import, sería de la siguiente manera: import name


import personas


personas.greeting("Camilo")

a = personas.people1["age"]
print(a)


from personas import people1

print (people1["age"])


import sys
print(sys.path)
#Imprime donde se está ejecuntando el archivo

import re
text = 'Mi numero de telefono es 311 123 121, el codigo del pais es 57, mi numero de la suerte 3'
result = re.findall('[0-9]+', text)
print(result)
#Esta expresión regular busca lo indicado dentro de [ ] 

import time
timestamp = time.time()
print(timestamp)
#hora actual en formato de computadora

local = time.localtime()
result = time.asctime(local)
print(result)
#Transforma el formato de hora

import collections
numbers = [1,1,2,1,2,1,4,5,3,3,21]
counter = collections.Counter(numbers)
print(counter)
#Devuelve un diccionario con el número de veces que se repite un item dentro de un elemento (frecuencia)