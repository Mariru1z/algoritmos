
vector = [1,2,3,4,5,6]#recibe la longitud del vector

a=len (vector)  #la longitud es de 6 elementos
print ("La longitud del vector es: ", a )#imprime la longitud del vector


#matriz vector de vectores
''''
import numpy as np
vector1=[1,2,3,4,5,6]
vector1=np.eye(6)
print(vector1)
'''
'''
#shape dimension de una matriz https://www.w3schools.com/python/numpy/numpy_array_shape.asp
#determina el numero de elementos 
import numpy as np
vector = np.array([1,2,3,4,5,6])
#print (vector.reshape(3,2))
#print (vector.reshape(-1,2))
#-1 es un comodín, si no quieres calcular, poner el -1
#vector - np.array ([1,2,3,4,5,6])
print(vector.shape)
print(vector.reshape(1,-1))
'''

'''
#numpy zeros, crear un arreglo de cero
import numpy as np

vector3=np.zeros((3,3))
print(vector3.shape)
print(vector3)
'''
'''
#numpy arg min 

import numpy as np

vector = np.array([1,2,3,4,5,6,-1])
print(np.argmin(vector))
'''
