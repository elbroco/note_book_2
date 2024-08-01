power_of = lambda x : x**2

print(power_of(5))

# funcion si es par o no

numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]

def es_par(num):
 if (num%2==0):
    return True

def es_impar(num):
 if (num%2==1):
    return True
# usando filter con una funcion comun

numeros_pares = filter(es_par,numeros)
print(list(numeros_pares))

numeros_impares = filter(es_impar,numeros)
print(list(numeros_impares))

# lo mismo pero con lambda

numeros_pares = filter(lambda numero:numero%2==0,numeros)
print(list(numeros_pares))

numeros_pares = filter(lambda numero:numero%2==1,numeros)
print(list(numeros_pares))
