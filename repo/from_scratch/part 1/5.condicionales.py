edad = 17

if edad >=18:
    print('eres mayor de edad')
else:
    print('eres menor de edad')

# if anidado(nested) = un if dentro de otro if 

ingreso_mensual = int(input("cual es tu ingreso mensual?"))
gasto_mensual = int(input("cual es tu gasto mensual mensual?"))

if ingreso_mensual > 10000:
    print('estas bien en cualquier parte del mundo')
    if gasto_mensual < 5000: # nested if
        print('estas bien')
    else:
        print('estas gastando mucho dinero bro')

elif ingreso_mensual > 1000:
    print('estas bien en latam')

elif ingreso_mensual > 500:
    print('estas bien en colombia')

elif ingreso_mensual > 200:
    print('estas bien en venezuela')

else:
    print('eres pobre')