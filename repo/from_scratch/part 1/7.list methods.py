# list = crea una lista

'''
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
'''

# es una funcion
lista = list(['hola','ivan',23,True,78,'holi',3.45])
print(lista)

# len = cuenta cuantos elementos hay en una lista
# es una funcion
print(len(lista))

# append = agrega un elemento
lista.append('hahaha')
print(lista)

# insert = agrega un elemento a la lista en una posicion especifica
lista.insert(2,'buena la rata') # indice,dato
print(lista)

# extend = agrega varios elementos a la lista
# se agregan en forma de lista
lista.extend([False,2023,'diomedes'])
print(lista)

# pop = elimina un elemento por su indice
# para eliminar el ultimo elemento de la list , se coloca -1
lista.pop(0)
lista.pop(-1)
print(lista)

# remove = elimina un elemento por su valor
lista.remove('buena la rata')
print(lista)

# sort = organiza elementos
# los elementos, tienen que ser solo strings o numericos(booleano,int o float)
# si colocamos reverese=True lo organiza a reves
lista.remove('ivan')
lista.remove('holi')
lista.remove('hahaha')
print(lista)
lista.sort()
print(lista)

lista.sort (reverse=True)
print(lista)
# reverse = no organiza, solo revierte la cadena sin importar su orden

lista.reverse()
print(lista)

# clear = elimina todos los elementos de una lista
lista.clear()
print(lista)