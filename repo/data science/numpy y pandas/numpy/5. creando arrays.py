"""

Numpy nos da varios métodos muy eficientes para poder crear arrays desde 0.

Este método de NumPy nos permite generar arrays sin definir previamente una lista.

>>>>np.arange(0,10)
---> array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

Un tercer argumento permite definir un tamaño de paso o salto.

>>>>np.arange(0,20,2)
---> array([ 0,  2,  4,  6,  8, 10, 12, 14, 16, 18])

>>>>np.zeros() Nos permite definir estructuras o esquemas.

np.zeros(3)
---> array([0., 0., 0.])
np.zeros((10,5))
---> array([[0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.]])
       
De igual manera, tenemos np.ones()

>>>>np.ones(3)
---> array([1., 1., 1.])


>>>>np.linspace() Permite generar una array definiendo un inicio, un final y cuantas divisiones tendrá.

np.linspace(0, 10 , 10)   filas, columnas, numero de datos 
--->  array([ 0.,1.11111111,2.22222222,  3.33333333,  4.44444444,
        5.55555556,  6.66666667,  7.77777778,  8.88888889, 10.])
        
        
También podemos crear una matriz con una diagonal de 1 y el resto de 0.  
>>>>np.eye(4)
----> array([[1., 0., 0., 0.],
             [0., 1., 0., 0.],
             [0., 0., 1., 0.],
             [0., 0., 0., 1.]])
       
Otro método importante es generar números aleatorios.
>>>>np.random.rand()
---> 0.37185218178880153

También se pueden generar vectores.
np.random.rand(4)
---> array([0.77923054, 0.90495575, 0.12949965, 0.55974303])

Y a su vez generar matrices.
np.random.rand(4,4)
---> array([[0.26920153, 0.24873544, 0.02278515, 0.08250538],
       [0.16755087, 0.59570639, 0.83604996, 0.57717126],
       [0.00161574, 0.27857138, 0.33982786, 0.19693596],
       [0.69474123, 0.01208492, 0.38613157, 0.609117  ]])
NumPy nos permite también generar números enteros.
En este caso números enteros entre el 1 y 14

>>>>np.random.randint(1,15)
---> 7
También podemos llevarlos a una estructura definida.

np.random.randint(1,15, (3,3))  rango para escoger el numero  ,   (filas,columnas)
---> array([[ 4,  2,  9],
           [ 5,  7,  8],
           [14, 14,  4]])
           
"""
