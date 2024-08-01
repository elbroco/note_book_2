# estructura para usar metodos = dato.metodo()

string1 = 'hola como estas?'
string2 = ' buenas buenas1 mis amigos y amigas'

# dir = devuelve la lista de atributos validos del objeto pasado
#print(dir(string1)) es una funcion, no un metodo


# upper = convierte en mayuscula
print(string1.upper())

# lower = convierte en minuscula
print(string1.lower())

# capitalize = primera letra en mayuscula
print(string1.capitalize())

# find = encuentra la primera aparicion del valor especificado sino devuelve -1
# busca una cadena en otra cadena
# es sensible a mayusculas y minusculas
print(string1.find('c')) # me devuelve la posicion donde esta

# index = encuentra la primera aparicion del valor especificado sino devuelve una excepcion
print(string1.find('a')) # find muestra -1 index muestra una excepcion

# isnumeric = si es numerico devuelve True
print(string1.isnumeric())

# isalpha = si es alfanumerico devuelve True
print(string1.isalpha())

# count = devuelve el numero de ocurrencias de una subcadena en la cadena dada
print(string1.count('a'))

# len = cuenta los caraceres de una cadena
# es una funcion
print(len(string1))

# endswith = verifica su una cadena termina con
print(string1.endswith('?'))

# startswith = verifica si una cadena comienza con 
print(string1.startswith("h"))

# replace = remplaza por otro valor
print(string1.replace("hola","hey"))
print(string1.replace(" ",","))

# split = separa por un parametro dado
# este metodo nos devuelve una lista o matriz
print(string1.split())

str_separada = string2.split()
print(str_separada[3])


