fruits = ['banana', 'apple','cranberry','orange','dragon fruit','peach']



for fruit in fruits:
    print (f' i am gonna eat a {fruit}')

print('bucle termninado')

# saltar un elemento en una iteracion
for fruit in fruits:
    if fruit == 'orange':
        continue
    print (f' i am gonna eat a {fruit}')

print('bucle termninado')

# evitar que el bucle siga ejecutandose
for fruit in fruits:
    if fruit == 'cranberry':
        break # if this condition occurs this stops the cycle
    print (f' i am gonna eat a {fruit}')

print('bucle termninado')

# recorrer una cadena de texto

string = 'buenas buenas'

for letter in string:
    print(letter)
print('bucle termninado')

# for en una solo linea de codigo
numeros = (2,4,6,8)
numeros_multiplicados = list()

for numero in numeros:
    numeros_multiplicados.append(numero*2)
    print(numeros_multiplicados)
print('bucle terminado')

# simplificando lo anterior
numeros_multiplicados = [x*2 for x in numeros]
print(numeros_multiplicados)

