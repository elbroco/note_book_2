# 0 filas/ 1 columnas

# Muestra las primeras 5 líneas del DataFrame
# df_books.head()
# ---> muestra las primeras 5 lineas del dataFrame

# Eliminar columnas de la salida pero no del DataFrame
# df_books.drop('Genre', axis=1).head()
# ---> #elimina la columna Genre de la salida pero no del dataFrame

# Eliminar una columna
# del df_books['Price']
# ---> #elimina la columna Price del dataFrame

# Eliminar filas
# df_books.drop(0, axis=0)
# ---> #elimina la fila 0 del dataFrame

# Eliminar un conjunto de filas mediante una lista
# df_books.drop([0,1,2], axis=0)
# ---> #elimina las filas 0, 1 y 2 del dataFrame

# Elimina un conjunto de filas mediante un rango
# df_books.drop(range(0,10), axis=0)
# ---> #elimina las primeras 10 filas del dataFrame

# Agregar una nueva columna con valores Nan  (valor no numerico)
# df_books['Nueva_columna'] = np.nan
# ---> #Crea una nueva columna con el nombre de Nueva_columna de valores Nan

# Mostrar el número de filas o columnas que tiene un DataFrame
# df_books.shape[0]
# ---> #Muestra el numero de filas que posee el dataFrame

# Agregar valores a una nueva columna
# data = np.arange(0, df_books.shape[0])
# Crear una nueva columna y agregar los valores almacenados en el array
# df_books['Rango'] = data
# ---> #Crea una nueva columna llamada Rango con los valores del array

# Para añadir filas se utiliza la función append de Python añadiendo como parámetro una lista, diccionario o añadiendo los valores manualmente.
# df_books.append(df_books)
# ---> #Duplica las filas del dataFrame porque se agrega a si mismo
