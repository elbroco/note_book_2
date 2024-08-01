def obtener_compas(cant_compas):
    compas = []
    for i in range(cant_compas):
        nombre = input('Ingrese el nombre del compa: ')
        edad = input('Ingrese la edad del compa: ')
        compa = (nombre, edad)
        compas.append(compa)
    compas.sort(key=lambda x: int(x[1]))  
    asistente = compas[0][0]
    profesor = compas[-1][0]
    return asistente, profesor

asistente, profesor = obtener_compas(5)

print(f'El profesor es: {profesor} y su asistente es {asistente}')
