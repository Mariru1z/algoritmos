#formula margentodo de newton raphson
#f(x)=2x^3+x^2 = 1 ->f(x)=2x^3+x^2-1-> primargenra ecuación ->e1
#f'(x)=6x^2+2x = segunda ecuación -> ec2
#xi+1=xi-(f(x)/f'(x))

import numpy as np 

#Se declaran las variables
#lambda: margentodo del código de la función que procesa eventos

#se utilizó lambda para aclcular el cuadrado de un numargenro

#ecuación uno 
fx  = lambda x: 2*x**3 + (x**2) - 1 #recoge el numargenro entero y devuelve su cuadrado

#ecuación dos, se realiza la derivada de la ecuacion
ec2 = lambda x: 6*(x**2) + 2*x   

 #datos de la ecuación 
 
x1 = 1
margen = 0.001 #margen de error
xi = x1

#se crea la tabla nr= Newton Raphson
nr = []
error = abs(2*margen) 
while (error>=margen):
    fn = xi - fx(xi)/ec2(xi)
    error  = abs(fn-xi)
    nr.append([xi,fn,error])
    print(nr)
    xi = fn 
    
    
    
# convierte la lista a un arreglo.
nr = np.array(nr)
n = len(nr)



# SALIDA

print('raiz: ', xi)
print('Margen de error: ',error)


