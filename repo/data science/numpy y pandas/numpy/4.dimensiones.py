"""
Con las matrices podemos crear varias dimensiones, vamos a nombrarlas


scalar: dim = 0 Un solo dato o valor

vector: dim = 1 Listas de Python

matriz: dim = 2 Hoja de cálculo

tensor: dim > 3 Series de tiempo o Imágenes


Scalar: 0 Un solo dato o valor
0

Vector: Listas de Python
0	1	2	3	4

Matriz: Hoja de cálculo
Color	País	Edad	Fruta
Rojo	España	24	Pera
Amarillo	Colombia	30	Manzana

Tensor: Series de tiempo o Imágenes
tensor

Declarando un escalar.
.ndim Nos muestra las dimensiones que tiene

scalar = np.array(42)
print(scalar) 
scalar.ndim 

---> 42
---> 0

Declarando un vector.
vector = np.array([1, 2, 3])
print(vector) 
vector.ndim 

---> [1 2 3]
---> 1
Declarando una matriz.
matriz = np.array([[1, 2, 3], [4, 5, 6]])
print(matriz)
matriz.ndim
----[[1 2 3]
    [4 5 6]]
---> 2
Declarando un tensor.
tensor = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],[[13, 13, 15], [16, 17, 18], [19, 20, 21], [22, 23, 24]]])
print(tensor)
tensor.ndim
---> [[[ 1  2  3]
  	[ 4  5  6]
  	[ 7  8  9]
 	[10 11 12]]

 	[[13 13 15]
  	[16 17 18]
  	[19 20 21]
        [22 23 24]]]	
---> 3
Agregar o eliminar dimensiones
Se puede definir el número de dimensiones desde la declaración del array

vector = np.array([1, 2, 3], ndmin = 10)
print(vector) 
vector.ndim 

---> [[[[[[[[[[1 2 3]]]]]]]]]]
---> 10
Se pueden expandir dimensiones a los array ya existentes con expand_dims(). Axis = 0 hace referencia a las filas, mientras que axis = 1 a las columnas.

expand = np.expand_dims(np.array([1, 2, 3]), axis = 0)
print(expand)
expand.ndim 

---> [[1 2 3]]
---> 2
Remover/comprimir las dimensiones que no están siendo usadas.

print(vector, vector.ndim) 
vector_2 = np.squeeze(vector)
print(vector_2, vector_2.ndim)

---> [[[[[[[[[[1 2 3]]]]]]]]]] 10
---> [1 2 3] 1

"""
