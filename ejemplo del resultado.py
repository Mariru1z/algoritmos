import numpy as  np

z= np.array([3,2,5])
A= np.array([[1,2,1],
             [3,0,2],
             [1,4,0]])
b=np.array([430,460,420])
print(z)
print(A)
print(b)

            
num_vars =len(z)
holgura_vars = len(b)

#np.eye(holgura_vars)

tabla_simplex = np.hstack((A, np.eye(holgura_vars), b.reshape(-1,1)))
print(tabla_simplex)



vectora = np.hstack((-z, np.zeros (holgura_vars+1)))
print(vectora)


vectora = np.hstack((-z, np.zeros (holgura_vars+1)))
tabla2_simplex=np.vstack((tabla_simplex, vectora))
print(tabla2_simplex)



#newton raphon 

 


#tabla2=np.hstack((z,z))

#print(tabla2)




