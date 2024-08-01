import paquete

print(type(paquete.__path__))


import paquete.saludar

print(paquete.saludar.saludar('camilo'))

