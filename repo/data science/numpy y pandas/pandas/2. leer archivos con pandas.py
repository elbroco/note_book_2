import pandas as pd

# En algunas ocasiones el archivo podría estar separado por " | " y se vería así.

# Para solucionar esto, usamos el atributo "Sep = ’ , ’ " y ya quedará bien organizado.
# pd.read_csv('/work/DataFrames/bestsellers-with-categories.csv', sep=  ' , ')

# Cambiar el encabezado, lo podemos hacer con “Header”, este pondrá de encabezado los valores que tenga en esa posición.
# pd.read_csv('/work/DataFrames/bestsellers-with-categories.csv', header = 2)


# Read the CSV file with new column names, treating the first row as data
df = pd.read_csv(
    r"C:\\Users\Alexandra la Mejor\Desktop\\python1\data science\\numpy y pandas\\numpy\\numpy\\numpy\\pandas\bestsellers-with-categories.csv",
    header=0,
    names=["Names", "Author", "User Rating", "Reviews", "Price", "Year", "Genre"],
)

# Print the first few rows of the DataFrame
print(df.head())


# json

# Para ***agregar un archivo ‘JSON’***, se hace de igual manera, pero en esta ocasión usamos

# pd.read_json('/work/DataFrames/hpcharactersdataraw.json')
# Lo único que cambió en nuestro código fue él 'read_json()'
