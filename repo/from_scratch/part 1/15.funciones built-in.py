# encontrando el numero mayor de una lista
numeros = [4,7,1,42,15]


# encontrando el numero mayor de una lista
mas_alto = max(numeros)
print(mas_alto)

# encontrando el numero menor de una lista
mas_bajo = min(numeros)
print(mas_bajo)


# redondeando a x numero de decimales
numero = float(1.23456)
print(round(numero,2))

# funcion bool
# retotna false 
# - si se le pasa un 0, false,vacio(listas,tuplas), none o ningun dato
# o true si se le coloca cuaquier otro elemento osea elementos verdaderos
resultado = bool(0)
print(resultado)

# funcion all
# retorna true si todos los valores son verdaderos
# comprueba cada elemento de un iterable

resultado = all(['dppd',True,84,87.44])
print(resultado)

# funcion sum
# suma todos los valores de un iterable

e = [2,4,56,-98,5]
resultado = sum(e)
print(resultado)
