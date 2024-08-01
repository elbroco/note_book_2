# el loop como tal recorre elementos
# hasta que no hay mas elementos
# iterar listas


animals = ['perro','loro','gato','lagarto']

numbers = [10,8,3,5,6,3.56]

for animal in animals:
    print(f'ahora la variable animal es igual a: {animal}')

for number in numbers:
    result = number * 10
    print(f'ahora es numero es: {result}')


# iterando dos listas
# tambien se pueden iterar mas de dos listas
for number,animal in zip(animals,numbers):
    print(f'recorriendo lista 1: {number}')
    print(f'recorriendo lista 1: {animal}')


# iterando valores
# termina en el penultimo valor

for num in range(5,11):
    print(num)

# forma correcta de recorrer una lista con su indice

for num in enumerate(numbers):
    print(num)

for num in enumerate(numbers):
    indice = num[0]
    valor = num[1]
    print(f'el indice es: {indice} y el valor es {valor}')


# usando el else

for number in numbers:
    print(f'ejecutando el ultimo bucle, valor actual: {number}')

else:

    print('el bucle termino')

# todo lo anterior funciona exactamente igual para tuplas y sets

# iterar un dictionario

diccionario = {
    'nombre' :'ivan',
    'apellido' : 'bolivar',
    'universidad' : 'unal'

}

for key in diccionario:
    print(key)

for key in diccionario.items():
    print(key)

# recorriendo un diccionario con items() para obtener la 
# clave y el valor
for datos in diccionario.items():
    key = datos[0]
    value = datos [1]
    print(f'la clave es: {key} y el valor es: {value}')


