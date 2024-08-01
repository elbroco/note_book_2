# super clases
class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print('Hola, estoy hablando.')

class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad

    def mostrar_habilidad(self):
        return f'Mi habilidad es: {self.habilidad}'

# sub clase con herencia múltiple
class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa 

    def presentarse(self):
        return f'hola soy {self.nombre}, trabajo en {self.empresa} y {super().mostrar_habilidad()}'


roberto = EmpleadoArtista('Roberto', 42, 'argentino', 'cantar', 100000, 'Microsoft')
print(roberto.presentarse())


#para saber si una subclase de una superclase
# si sale true entonce si es subclase primero va la sub clase y 
# luego la super clase

herencia = issubclass(EmpleadoArtista,Artista)
print(herencia)

herencia = issubclass(Persona,Artista)
print(herencia)


# para saber si un objeto es una instancia de una clase utilizamos

instancia = isinstance(roberto,EmpleadoArtista)
print(instancia)

instancia = isinstance(roberto,Artista)
print(instancia)




