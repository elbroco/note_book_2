"""

Shape
Indica la forma del arreglo.

arr = np.random.randint(1,10,(3,2))
arr.shape
---> (3, 2)
arr
---> array([[4, 2],
          [4, 8],
          [4, 3]])
Reshape
transforma el arreglo mientras se mantengan los elementos.

arr.reshape(1,6)
----> array([[4, 2, 4, 8, 4, 3]])
arr.reshape(2,3)
---> array([[4, 2, 4],
          [8, 4, 3]])
np.reshape(arr,(1,6))
---> array([[4, 2, 4, 8, 4, 3]])

c y f
https://static.platzi.com/media/user_upload/Captura%20de%20pantalla%202023-12-09%20164103-7514780b-bbb0-453c-8b71-782f1cdfd74d.jpg
Se puede hacer un reshape como lo haría C. 

np.reshape(arr,(2,3), 'C') Cuando apilamos los valores mediante el lenguaje C, apilamos mediante filas:

---> array([[4, 2, 4],
       [8, 4, 3]])
También se puede hacer reshape a como lo haría Fortran. Cuando apilamos los valores a través de Fortran, apilamos mediante columnas:

np.reshape(arr,(2,3), 'F')
---> array([[4, 4, 8],
       [4, 2, 3]])
Además, existe la opción de hacer reshape según como esté optimizado nuestro computador. En este caso es como en C.

np.reshape(arr,(2,3), 'A')
---> array([[4, 2, 4],
       [8, 4, 3]])
No puedes cambiar la "forma" a la "forma" original del array, si tienes un (3,3) no lo puedes pasar a (4,2). 
No respeta los 9 elementos del array original

"""

import numpy as np

arr = np.random.randint(66, 77, (1, 10))

print(arr)
print(arr.shape)
print("....\n")

arr = arr.reshape(2, 5)
print(arr.shape)

print(arr)
