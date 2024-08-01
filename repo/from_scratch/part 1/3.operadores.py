# operadores matematicos
a = 3
b = 10

print (a+b)# suma
print (b-a)# resta
print (a*b)# multiplicacion
print (b/a)# division
print (b**a)# potenciacion
print (b%a)# modulo = me da el resto de la division
print (b//a)# division baja = devuelve el entero redondeado hacia abajo

# operadores de comparacion

igual_que =     5 == 6
distinto_de =   5 != 6
mayor_que =     5 > 6
menor_que =     5 < 6
mayor_o_igual = 5 >= 6
menor_o_igual = 5 <= 6

# esto me devuelve true o false

print(distinto_de)
print(mayor_o_igual)

# calculos combinados

a = 5
b = 10
c = 30

compare = a + b < c

print(compare)

# comparar usuario

usuario_de_base_de_datos = 'ivan b'
usuario_escrito = 'lucas'

if usuario_de_base_de_datos == usuario_escrito:
    print ('welcome')
else:
    print('access denied')

# comparar password

password = 'hola123'
password_given = 'hola123k'

compare = password == password_given
print(compare)

if password == password_given:
    print('welcome')
else:
    print('access denied')

