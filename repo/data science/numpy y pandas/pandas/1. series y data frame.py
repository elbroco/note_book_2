"""

Series y DataFrames en Pandas
Ya entendiste los conceptos básicos de Numpy,
ahora hay que entender como funciona la 
librería de Pandas, esta nos ayuda a hacer 
una mejor exploración y análisis de los datos.

Pandas
Pandas es una librería de Python especializada 
en el manejo y análisis de estructuras de datos.
El nombre viene de “Panel data”.

• Velocidad
• Poco código
• Múltiples formatos de archivos
• Alineación inteligente

Pandas Series
Es muy parecido a un array de una dimensión 
(o vector) de NumPy.

• Arreglo unidimensional indexado
• Búsqueda por índice
• Slicing
• Operaciones aritméticas
• Distintos tipos de datos

Pandas DataFrame
Muy parecido a las estructuras matriciales
trabajadas con NumPy.

• Estructura principal
• Arreglo de dos dimensiones
• Búsqueda por índice (columnas o filas)
• Slicing
• Operaciones aritméticas
• Distintos tipos de datos
• Tamaño variable

Series
Es un arreglo unidimensional indexado

import pandas as pd
Definiendo una lista con índices específicos

psg_players = pd.Series(['Navas','Mbappe','Neymar','Messi'], index=[1,7,10,30])

psg_players 
---> 1      Navas
     7     Mbappe
     10    Neymar
     30     Messi
     dtype: object 
     
        
Búsqueda por índices

dict = {1: 'Navas', 7: 'Mbappe', 10: 'Neymar', 30:'Messi'}
pd.Series(dict)
---> 1 Navas
7 Mbappe
10 Neymar
30 Messi
dtype: object

psg_players[7]
----> 'Mbappe'


Búsqueda mediante Slicing

psg_players[0:3]
-----> 0     Navas
       1    Mbappe
       2    Neymar
    dtype: object
Pandas


Similar a la estructura matricial

dict = {'Jugador':['Navas','Mbappe','Neymar','Messi'],
 'Altura':[183.0, 170.0, 170.0, 163.0],
  'Goles':[2, 200, 150, 500]}
df_players = pd.DataFrame(dict, index=[1,7,10,30])


--->   Jugador Altura Goles
        1 Navas    183    2
        7 Mbappe   170    200
        10 Neymar   170    150
        30 Messi    163    500
        
        
Búsqueda por índices. Columnas

df_players.columns
---> Index(['Jugador', 'Altura', 'Goles'], dtype='object')


Búsqueda por índice.

df_players.index
------> RangeIndex(start=0, stop=4, step=1)


"""

import pandas as pd

import pandas as pd

group = {
    "name": ["Luis", "Jorge", "Antonia", "German", "Luisa", "Manuel"],
    "gender": ["H", "H", "M", "M", "H", "H"],
    "age": [19, 23, 11, 64, 35, 16],
    "Altura": [185.0, 187.0, 185.0, 187.0, 175.0, 190.0],
    "profesion": [
        "programmer",
        "salesperson",
        "real-state owner",
        "physicist",
        "Luisa",
        "Manuel",
    ],
}

# Create the DataFrame and assign specific row indices
df_group = pd.DataFrame(group, index=[1, 7, 10, 30, 32, 33])

# Print the DataFrame
print(df_group)

# Print the DataFrame index
print(df_group.index)

print(df_group.iloc[2])
