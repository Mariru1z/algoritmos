import numpy as  np

#pide las A del vector
A = int(input("Ingrese el numero de A de la primera fila: "))

#crear la primera fila del vector

vector = np.zeros(A)

#cada dimension a llenar

for i in range(A):
    print(f"Ingrese el valor de la dimension {i+1}:")
    vector[i] = float(input())
    
    print(vector)



