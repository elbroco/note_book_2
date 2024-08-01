# Exception	Description
# ArithmeticError	Se genera cuando se produce un error en los cálculos numéricos
# AssertionError	Se genera cuando falla una declaración de afirmación
# AttributeError	Se genera cuando falla la asignación o la referencia de atributo
# Exception	Clase base para todas las excepciones
# EOFError	Se genera cuando el método input() alcanza una condición de "fin de archivo" (EOF)
# FloatingPointError	Se genera cuando falla un cálculo de punto flotante
# GeneratorExit	Se genera cuando se cierra un generador (con el método close())
# ImportError	Se genera cuando no existe un módulo importado
# IndentationError	Se genera cuando la sangría no es correcta
# IndexError	Se genera cuando no existe un índice de una secuencia
# KeyError	Se genera cuando una clave no existe en un diccionario
# KeyboardInterrupt	Se genera cuando el usuario presiona Ctrl+c, Ctrl+z o Eliminar
# LookupError	Se genera cuando no se pueden encontrar los errores generados
# MemoryError	Se genera cuando un programa se queda sin memoria
# NameError	Se genera cuando una variable no existe
# NotImplementedError	Se genera cuando un método abstracto requiere una clase heredada para anular el método
# OSError	Se genera cuando una operación relacionada con el sistema provoca un error
# OverflowError	Se genera cuando el resultado de un cálculo numérico es demasiado grande
# ReferenceError	Se genera cuando no existe un objeto de referencia débil
# RuntimeError	Se genera cuando ocurre un error que no pertenece a ninguna expectativa específica
# StopIteration	Se genera cuando el método next() de un iterador no tiene más valores
# SyntaxError	Se genera cuando se produce un error de sintaxis
# TabError	Se genera cuando la sangría consta de tabulaciones o espacios
# SystemError	Se genera cuando se produce un error del sistema
# SystemExit	Se genera cuando se llama a la función sys.exit()
# TypeError	Se genera cuando se combinan dos tipos diferentes
# UnboundLocalError	Se genera cuando se hace referencia a una variable local antes de la asignación
# UnicodeError	Se genera cuando se produce un problema Unicode
# UnicodeEncodeError	Se genera cuando se produce un problema de codificación Unicode
# UnicodeDecodeError	Se genera cuando se produce un problema de decodificación Unicode
# UnicodeTranslateError	Se genera cuando se produce un problema de traducción Unicode
# ValueError	Se genera cuando hay un valor incorrecto en un tipo de datos especificado
# ZeroDivisionError	Se genera cuando el segundo operador en una división es cero

# lanzar errores propios con raise
age = 10
if age < 18:
  raise Exception('No se permiten menores de edad')
#--> Exception: No se permiten menores de edad



#apesar de generar un error continua con el codigo

try:
  print(0 / 0)
  assert 1 != 1, 'Uno no es igual que uno'
  age = 10
  if age < 18:
    raise Exception('No se permiten menores de edad')
except ZeroDivisionError as error:
  print(error)
except AssertionError as error:
  print(error)
except Exception as error:
  print(error)

print('Hola')
print('Hola 2')

try:
    pass
except Exception as e:
    raise
else:
    pass
finally:
    pass

# . El bloque else se ejecuta cuando todo lo del bloque ‘try’ se ejecuta correctamente,
# es decir, sin excepciones. 
# . El bloque finally se ejcuta haya o no excepciones en el bloque
# ‘try’, es decir, que su ejecución es obligatoria

def my_divide(a, b):
  # Escribe tu solución 👇
  try:
    result = a / b
  except ZeroDivisionError as error:
    result = 'No se puede dividir por 0'
  return result

response = my_divide(10, 2)
print(response) # 5

response = my_divide(10, 0)
print(response)


