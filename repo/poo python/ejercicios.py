#Ejercicio 1
'''
class Estudiante:
    def __init__(self, nombre, edad, grado):
       self.nombre = nombre
       self.edad = edad
       self.grado = grado

    def estudiar(self):
        print(f'el estudiante {self.nombre} esta estudiando')  





name = input(f'cual es el nombre del estudiante?: \n')
age = input(f'cual es la edad del estudiante?: \n')
grade = input(f'en que grado esta el estudiante?: \n')

Estudiante1 = Estudiante(name,age,grade)


Estudiante1.estudiar()

print(Estudiante1.nombre)
print(Estudiante1.edad)
print(Estudiante1.grado)
'''
# ejercicio 2

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def introduce(self):
        print(f'Hola me llamo {self.nombre} y mi edad es {self.edad}')


class Estudiante(Persona):

    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado

    def tell_grade(self):
        print(f'Mi grado es {self.grado}')

Ivan = Estudiante("Roberto", 23, "noveno")

print(Ivan.nombre)
print(Ivan.edad)
print(Ivan.grado)

Ivan.introduce()
Ivan.tell_grade()


# ejercicio 3


class Animal:
    def comer(self):
        print('el animal está comiendo')

class Mamífero(Animal):
    def amamantar(self):
        print('el mamifero está amamantando')

class Ave(Animal):
    def volar(self):
        print('el ave está volando')

class Murciélago(Mamífero, Ave):
    def hablilidades(self):
        super(Mamífero, self).amamantar()
        super(Ave, self).volar()

murciélago = Murciélago()

murciélago.comer()
murciélago.amamantar()
murciélago.volar()




print(Murciélago.mro()) # nos da el orden de jerarquia