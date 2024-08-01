# existe clase padre y clase hija o super clase y sub clase

# clase padre
class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print('hola estoy hablando xd')

# clase hija (esta hereda todos los atributos de la clase padre)
# si no quiero agregar mas cosas le coloco pass
# y de esa forma se creo un clase hija

# asi se contruye una clase hija (sub clase)
# diciendole que quiere que se herede
# esto se llama herencia simple

class Empleado (Persona):
#     pass 

    def __init__(self,nombre,edad,nacionalidad,trabajo,salario):
        super().__init__(nombre,edad,nacionalidad)
        self.trabajo = trabajo
        self.salario = salario




roberto = Empleado("roberto",23,"colombiano",'programador','100000')

print(roberto.nombre)
print(roberto.edad)
print(roberto.nacionalidad)
print(roberto.trabajo)
print(roberto.salario)


roberto.hablar()


# herencia jerarquica
# hay una super clase que tiene varias subclases

class Estudiante (Persona):
    def __init__(self,nombre,edad,nacionalidad,notas,universidad):
        super().__init__(nombre,edad,nacionalidad)
        self.notas = notas
        self.universidad = universidad

# herencia multiple
# una clase hereda  de dos clases

class PersonaNormal (Empleado,Estudiante):
    pass



