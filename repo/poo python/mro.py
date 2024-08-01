#method resolution order

class A:
    def hablar (self):
        print('hola desde A')

class B(A):
#    def hablar (self):
#        print('hola desde B')
 pass

class C(A):
#    def hablar (self):
#        print('hola desde C')
 pass

class D(B,C):
#    def hablar (self):
#        print('hola desde D')
 pass

# al poner esto (A) significa que estan heredando de la clase A

d = D()



# primero le da prioridad a A porque es la funcion que llamamos, despues  B debido a (b,c) , y luego
# a C y  por ultimo a A
#  D > B > c > A

print(D.mro()) # nos da el orden de jerarquia

