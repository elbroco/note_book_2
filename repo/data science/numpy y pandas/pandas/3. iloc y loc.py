import pandas as pd


# Cuando queremos navegar por un dataFrame estas funciones permiten filtrar datos de manera más específica

# .loc
# Filtra según un label

import pandas as pd

# Read the CSV file with corrected file path and specified separator
df_books = pd.read_csv(
    r"C:\Users\Alexandra la Mejor\Desktop\python1\data science\numpy y pandas\numpy\numpy\numpy\pandas\bestsellers-with-categories.csv",
    sep=",",
    header=0,
)

# Select all rows and print
print(df_books.loc[:])
# ---> #muestra todos los datos del dataFrame

# Mostrar un rango de filas tomando en cuenta el start y el end

df_books.loc[6:12]
print(df_books.loc[6:12])
# ---> #muestra los datos de la fila 0 a la fila 4

# Filtrando por filas y columnas
df_books.loc[0:4, ["Name", "Author"]]
print(df_books.loc[0:4, ["Name", "Author"]])
# ----> #filtra los datos de la fila que va de 0 a 4 y de las columnas Name y Author

# Podemos modificar los valores de una columna específica del dataFrame
# df_books.loc[:, ['Reviews']] * -1
# ---> #multiplica por -1 todos los valores de la columna Reviews

# Filtrar datos que cumplan una condición determinada
# df_books.loc[:, ['Author']] == 'JJ Smith'
print(df_books.loc[0:5, ["Author"]] == "JJ Smith")
# ----> #muestra la columna Author con True en los valores que cumplen la condicion y False para los que no la cumplen


# .iloc
# Filtra mediante índices.

# df_books.iloc[:] ---> #muestra todos los datos del dataframe

# Filtrar datos según los índices de las filas y las columnas
# df_books.iloc[:4, 0:2] ---> #muestra los datos de las filas que van de 0 a 3 y las columnas con indices 0 y 1

# Buscar un dato específico.
# df_books.iloc[1,3] ---> #muestra el dato alojado en la fila 1 columna 3
