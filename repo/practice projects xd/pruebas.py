def category(name,age):
    if 0 < age <= 11:
      a = 'infancy'
    elif 11 < age <= 18:
      a = 'teenage phase'
    elif 19 < age <= 26:
      a = 'young adulthood'
    elif 27 < age <= 59:
      a = 'adultez'
    elif 59 < age :
      a = 'vejez'
    else:
      print('valor invalido')

    return a


name = input('cual es tu nombre?: ')
age = int(input('cual es tu edad?: '))
resultado = category(name,age)
print(f'hola {name} te encuentras en la etapa de la {resultado}')

