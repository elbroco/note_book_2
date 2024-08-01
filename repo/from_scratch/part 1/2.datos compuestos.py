#conclusion = todos pueden ser iterados
# a las listas se les puede mover y cambiar elementos
# a las tuplas no se les puede hacer eso
# a los conjuntos o sets solo se les puede mover elementos y
# no deja acceder al indice como en las listas o tuplas, ni deja
#repetir valores

# la lista va con brackets 
lista = ['ivan','unal',True,1.73] 

# para sacar un item de una lista, la numeracion
# empieza desde cero
# las listas se pueden modificar
lista[1] = 'los andes'
print(lista[1])

tupla = ('ivan','unal',True,1.73) 
#tupla[1] = 'los andes' esto genera error
print(tupla[1])
# la lista va con parentesis
# las tuplas no se pueden modificar, sale error

# creando un set, va con llaves

conjunto = {'ivan','unal',True,1.73}

# creando un dictionario
# va con llaves
# la estructura del diccionario es key : value
# se llama la key y te da el value

diccionario = {
'nombre' : 'ivan',
'universidad' : 'unal',
'programa_?' : True,
'altura' : 1.73
} 

print(diccionario['altura'])
