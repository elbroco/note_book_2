class Gato:
    def sonido(self):
        return "miau"

class Perro:
    def sonido(self):
        return "guau"

gato = Gato()
perro = Perro()

'''
polimorfismo se refiere a que distintos objetos realizan un metodo y generan un dato distinto

# Llama a los métodos sonido y muestra su resultado

print(gato.sonido())
print(perro.sonido())
'''

# en este tipo de polimorfismo solo cambia el parametro
def hacer_sonido(animal):
    print(animal.sonido())

hacer_sonido(gato)
hacer_sonido(perro)


