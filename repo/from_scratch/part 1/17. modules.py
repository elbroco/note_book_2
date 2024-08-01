#un modulo seria cualquier archivo .py

# modulos de python
# modulos de terceros
# modulos propios

# utilizando un modulo
import modulo_saludar

saludo0 = modulo_saludar.saludar("camilo")
print(saludo0)

# utilizando as
# sirve para cambiar el nombre de los modulos
# tambien sirve para cambiar el nombre de las funciones importadas

import modulo_saludar as hello

saludo = hello.saludar('john')
print(saludo)

# se puede importar varias funciones
from modulo_saludar import saludar,saludar_informal

saludo = saludar('craig')
print(saludo)

saludo = saludar_informal('roy')
print(saludo) 


# check stuff about module routing

import sys 
print(sys.path)
