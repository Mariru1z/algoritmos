
import numpy as  np
# Pedir al usuario que ingrese las dimensiones del vector
dimensiones = int(input("Por favor, ingrese el número de dimensiones del vector: "))

# Crear un vector con las dimensiones especificadas por el usuario
vector = np.zeros(dimensiones)

# Preguntar al usuario por cada dimensión y llenar el vector
for i in range(dimensiones):
    print(f"Ingrese el valor para la dimensión {i+1}:")
    vector[i] = float(input())

# Verificar si el vector es correcto

print (vector)