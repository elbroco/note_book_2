"""
Las condiciones nos permiten hacer consultas más específicas.

arr = np.linspace(1,10,10, dtype = 'int8') 
# desde que valor rango, hasta que valor, cuantos elementos
arr 
---> array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10], dtype=int8)


Regresa un array de booleanos dónde la condición se cumple.
indices_cond = arr > 5
indices_cond
---> array([False, False, False, False, False,  True,  True,  True,  True, True])

Regresa los valores para dónde la condiciones True.
arr[indices_cond] 
---> array([ 6,  7,  8,  9, 10], dtype=int8)

Múltiples condiciones.
arr[(arr > 5) & (arr < 9)] 
---> array([6, 7, 8], dtype=int8)

Modificar los valores que cumplan la condición.
arr[arr > 5] = 99
arr
---> array([ 1,  2,  3,  4,  5, 99, 99, 99, 99, 99], dtype=int8)
"""

import numpy as np

array = (np.linspace(1, 10, 10)).astype(int)
print(array)

arr_cond = array % 2 == 0
numbers_arr = array[arr_cond]

print(numbers_arr)
