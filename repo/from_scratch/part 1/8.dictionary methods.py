diccionario = { 
    'nombre': 'Ivan',
    'apellido': 'Bolivar',
    'universidad': 'UNAL'
}
'''
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
# keys = devuelve las keys, tambien nos sirve para iterar
print(diccionario.keys())
'''

# get = devuelve el value, en el parentesis se coloca la key
# sino encuentra nada el programa continua
print(diccionario.get('nombre'))

# pop = elimina un elemento
diccionario.pop('apellido')
print(diccionario)

# items = para iterar el dict
# nos devuelve el diccionario
# iterar es recorrer elementos

diccionario_iterable = diccionario.items()
print(diccionario_iterable)# si se puede iterar
print(diccionario)# no se puede iterar

# clear = elimina todos los elementos del diccionario
diccionario.clear()
print(diccionario)

