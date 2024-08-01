class Celular():
    marca = 'Samsung'
    modelo = 'S23'
    camara = '48MP'

# estos son atributos estaticos 

# un objeto es una instancia de una clase 

celular1 = Celular()
celular2 = Celular()
celular3 = Celular()

print(celular1.marca)
print(celular2.modelo)
print(celular3.camara)


print('otro concepto')

# funcion construtora

class Celular:
    def __init__(self, marca, modelo, camara):
       self.marca = marca
       self.modelo = modelo
       self.camara = camara

    def llamar(self):
        print(f'Estas haciendo un llamado desde un: {self.modelo}')  

    def cortar(self):
        print(f'cortaste la llamada desde un: {self.modelo}')




celular1 = Celular('samsung','S23','48MP')
celular2 = Celular('apple','Iphone 15','98MP')


print(celular1.marca)
print(celular2.marca)

# un objeto puede tener atributos (propiedades) y tambien metodos (acciones)
# todas las funciones creadas dentro de una clase es un metodo
# la funcion __init__ le da propiedades a un objeto 


celular1.llamar()
celular2.cortar()