# desempaquetado de variables
# se puede hacer con listas, tuplas 

# tupla
datos = ('ivan','bolivar','unal') 

nombre,apellido,universidad = datos

print(apellido)

# lista
datos = ['ivan','bolivar',23]

nombre,apellido,edad = datos

print(edad)


# creando una tupla con tuple

tupla = tuple(['dato1','dato2'])

# otra forma de crear una tupla sin parentesis y mutiples datos

tupla1 = 'dato1','dato2'
print(tupla1)

# creando una tupla de un solo dato
tupla2 = 'dato1',


# creando un conjunto con set
 
conjunto = set(['perro','pato'])

print(conjunto)

# metiendo un conjunto dentro de otro conjunto
# es necesario utilizar la funcion frozenset
conjunto1 = frozenset(['galleta', 'paleta'])
conjunto2 = {conjunto1,'jugo'}

print(conjunto2)

# teoria de conjuntos


# verificar si es un sub-conjunto
# para saber si es un super conjunto se utiliza la funcion
# issuperset()
set1 = {1,3,5,7}
set2 = {1,3,7}

result = set2.issubset(set1)
print(result)

result = set1 <= set2
print(result)

# verificar si hay un numero en comun
# si sale true es porque los conjuntos son disyuntos
# si sale false es porque hay al menos un elemento en
# comun
resultado = set1.isdisjoint(set2)
print(result)

# crear diccionarios con dict()

diccionario = dict(nombre='ivan',apellido='bolivar')

print(diccionario)

#las listas no pueden ser keys a no ser que se use
# frozenset, pero las tuplas si

# crando diccionarios con fromkeys()

diccionario = dict.fromkeys(['nombre','apellido','edad','universidad'])
print(diccionario)

diccionario = dict.fromkeys(['nombre','apellido','edad','universidad'], 'indefinido')
print(diccionario)


#para crear cualquier tipo de dato vacio hay que usar 
#su funcion caracteristica list(),tuple(),dict()











