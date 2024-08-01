# creando una funcion simple

 
def saludar():
    print('que pasa bro?')

# ejecutando la funcion simple
saludar()


# funcion con parametros

def saludar(nombre):
    print(f'hey que pasa {nombre}')

saludar('ivan')

def saludar(nombre,sexo):
    sexo = sexo.lower()
    if (sexo == 'mujer'):
     adj = 'reina'
    elif (sexo == 'hombre'):
     adj = 'rey'
    else:
     adj = 'amor'


    print(f'Hola {nombre}, mi {adj} que tal?')

name = (input("cual es tu nombre?  "))
gender = (input("cual es tu genero?  "))

saludar(name,gender)


# crear una funcion que nos retorne valores

def random_pasword(num):
    chars = "abcdefghij"
    num_entero = str(num)
    num =int(num_entero[0])
    c1 = num - 2
    c2 = num 
    c3 = num - 5
    password = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*12}"
    return password


password = random_pasword(78)
print(password)



def suma (a,b):
    return a+b

resultado = suma(5,3)

print(resultado)

# utilizando el parametro *args
# convierte en parametros

def suma (*numeros):
    return sum(numeros)

resultado = suma(5,3,8,9,5,-6)
print(resultado)

# *args y otras variables


def suma (nombre,*numeros):
    return f"{nombre}, la suma de los numeros es: {sum(numeros)}"

resultado = suma('lucas',5,3,8,9,5,-6)
print(resultado)


# sumar un lista


def suma_total (numeros):
    return sum([*numeros])

resultado2 = suma_total([5,3,8,9,5,-6])
print(resultado2)

# otros ejemplos

def frase(nombre,apellido,adjetivo):
    return f'hola {nombre} {apellido}, sos muy {adjetivo}'


frase_resultante = frase('lucas','paez','crack')
print(frase_resultante)

# mismo ejemplo orden distinto


def frase(nombre,apellido,adjetivo):
    return f'hola {nombre} {apellido}, sos muy {adjetivo}'


frase_resultante = frase(adjetivo ='crack',apellido='paez', nombre='ivan')
print(frase_resultante) 
