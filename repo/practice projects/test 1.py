
# Crear listas vacías para los alumnos
alumno1 = []
alumno2 = []
alumno3 = []

# Recopilar información del primer alumno
nombre1 = input('Nombre del primer alumno: ')
apellido1 = input('Apellido del primer alumno: ')
edad1 = int(input('Edad del primer alumno: '))

# Agregar la información del primer alumno a la lista
alumno1.append((nombre1, apellido1, edad1))

# Recopilar información del segundo alumno
nombre2 = input('Nombre del segundo alumno: ')
apellido2 = input('Apellido del segundo alumno: ')
edad2 = int(input('Edad del segundo alumno: '))

# Agregar la información del segundo alumno a la lista
alumno2.append((nombre2, apellido2, edad2))

# Recopilar información del tercer alumno
nombre3 = input('Nombre del tercer alumno: ')
apellido3 = input('Apellido del tercer alumno: ')
edad3 = int(input('Edad del tercer alumno: '))

# Agregar la información del tercer alumno a la lista
alumno3.append((nombre3, apellido3, edad3))

# Encontrar al alumno más viejo usando max y una función lambda para seleccionar la edad
oldest = max([alumno1, alumno2, alumno3], key=lambda x: x[0][2])
youngest = min([alumno1, alumno2, alumno3], key=lambda x: x[0][2])

print(f"El profesor es: {oldest[0][0]} {oldest[0][1]}, con {oldest[0][2]} años.")
print(f"El asistente es: {youngest[0][0]} {youngest[0][1]}, con {youngest[0][2]} años.")

a = sorted([alumno1[0], alumno2[0], alumno3[0]])

for alumno in a:
    nombre = alumno[0]
    apellido = alumno[1]
    edad = alumno[2]
    print(f'Nombre: {nombre}, Apellido: {apellido}, Edad: {edad}')


