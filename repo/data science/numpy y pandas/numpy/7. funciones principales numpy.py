"""
Vamos a ver cuáles son las funciones que se utilizan 
normalmente con NumPy cuando analizamos los datos.

arr = np.random.randint(1, 20, 10)
arr
---> array([ 6, 11, 15, 12,  9, 17,  7,  7, 12,  3])

matriz = arr.reshape(2,5)
matriz
---> array([[ 6, 11, 15, 12,  9],
       [17,  7,  7, 12,  3]])
       
       
.max Para el máximo

arr.max() ----> 17
matriz.max() ----> 17

Podemos regresar los máximos de cada fila o columna
especificando el eje

Recuerda que:

0	Columnas
1	Filas
matriz.max(1) ---> array([15, 17])
matriz.max(0) --->rray([17, 11, 15, 12,  9])


También tenemos .argmax() que nos devuelve la
posición del elemento

arr.argmax() ---> 9
En el caso de la matriz nos muestra con un 1 dónde 
se encuentra el mayor entre las columnas

matriz.argmax(0) ---> array([0, 1, 1, 0, 1])


De forma análoga tenemos .min()

arr.min() ---> 3
arr.argmin() ---> 3
matriz.min(0) ---> array([ 6,  7,  7, 12,  3])
matriz.argmin(1) ---> array([6, 3])


Podemos saber la distancia entre el valor más bajo
con el más alto.

arr.ptp() # 17 - 3 ---> 14
matriz.ptp(0)  ---> array([11,  4,  8,  0,  6])


Análisis estadístico
Ordenar los elementos:

arr.sort() ---> array([ 3,  6,  7,  7,  9, 11, 12, 12, 15, 17])


Obtener un percentil:

np.percentile(arr, 50) ---> 10.0

Mediana:

np.median(arr) ---> 10.0

Desviación estándar:

np.std(arr) ---> 4.0853396431631

Varianza:

np.var(arr) ---> 16.69

Promedio:

np.mean(arr) ---> 9.9

Lo mismo aplica para las matrices.

np.median(matriz, 1) ---> array([ 7., 12.])


Concatenación
Se pueden unir dos arrays

a = np.array([[1,2], [3,4]])
b= np.array([5, 6])
np.concatenate((a,b), axis = 0)

---> ValueError: all the input arrays must have same 
number of dimensions, but the array at index 0 has 2
dimension(s) and the array at index 1 has 1 dimension(s)
El error anterior es debido a que ‘a’ tiene 2 dimensiones,
mientras que ‘b’ tiene 1.

a.ndim ---> 2
b.ndim ---> 1
Debemos poner ‘b’ en 2 dimensiones también.

b = np.expand_dims(b, axis = 0)
np.concatenate((a,b), axis = 0)
---> array([[1, 2],
             [3, 4],
             [5, 6]])
De igual manera, podemos agregarlo en el otro eje

np.concatenate((a,b), axis = 1)

ValueError: all the input array dimensions for the 
concatenation axis must match exactly, but along 
dimension 0, the array at index 0 has size 2 and 
the array at index 1 has size 1
Como ‘b’ es una fila y no una columna, no se puede 
concatenar a menos que se aplique la transpuesta.

La transpuesta pone nuestro array en sentido opuesto,
si el array original es (1,2), con la transpuesta
quedará (2,1)


transpuesta de una matrix 
b.T  
---> array([[5],
           [6]])
np.concatenate((a,b.T), axis = 1)
---> array([[1, 2, 5],
               [3, 4, 6]])

"""
