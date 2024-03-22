

''''
#crear un codigo que resulva  maxz = 2x1+3x2+4x3 + 5x4 por metodo simplex?

#pedir al usuario que ingrese el numero de filas y ,columnas para la matriz


#pide el numero de fils y columnas
numero_filas = int (input("Ingresa el numero de filas para tu matriz:->"))
numero_columnas = int(input("ingresa el numero de columnas para tu matriz: ->"))
 
 #inicia la matriz
 
matrix = []
 
 #insertar los valores de la matriz
for i in range(0,numero_filas):
    fila = []
    for j in range(0,numero_columnas):
         valor = int(input (f"Valor para la fila {i+1}, columna {j+1} ->")) #f-string         
         fila.append(valor)
    matrix.append(fila)
    print(matrix)
    
# se imprime la matriz

for fila in matrix:
    print(fila)
    
    # Encuentra el valor mínimo en la primera fila
min_valor = min(matrix[0])

# Encuentra la posición del valor mínimo de l aprimera fila

indice_min = matrix[0].index(min_valor)
print(f"El coeficiente mas negativo en el renglon de la funcion objetivo en las variables de decision es: {min_valor}")
print(f"Se encuentra en el renglon de la funcion objetivo  {indice_min + 1}")


# Imprime la columna correspondiente al valor mínimo
print(f"Columna pivote es:")
for fila in matrix:
    print(fila[indice_min])
    
# Divide la columna del renglón del valor mínimo por la última columna
columna_pivote = [fila[indice_min] / fila[-1] for fila in matrix]

# Encuentra la fila con el mayor resultado
indice_fila_pivote = columna_pivote.index(max(columna_pivote))

print(f"La columna pivote es: {columna_pivote}")
print(f"La fila pivote es la fila {indice_fila_pivote + 1} con el mayor resultado.")
'''
import numpy as np

# Objective function coefficients
c = np.array([2, 3, 4, 5])

# Constraint matrix
A = np.array([[1, 1, 1, 1],  # Constraint 1
              [0, 1, 2, 3],  # Constraint 2
              [2, 1, 0, 0]])  # Constraint 3

# Right-hand side vector
b = np.array([4, 11, 8])

# Basic variables
basic = np.array([0, 1, 2])

# Non-basic variables
non_basic = np.array([3, 4])

# Initial tableau
tableau = np.zeros((len(c), len(c) + len(b) + 1))
tableau[:len(c), :len(c)] = np.diag(c[non_basic])
tableau[:len(c), -len(b)-1] = -c[basic]
for i in range(len(b)):
    tableau[i, -len(b)+i] = 1
    tableau[i, -1] = b[i]

# Revised simplex method
while True:
    # Find the index of the most negative element in the bottom row
    min_ratio_index = np.argmin(tableau[-1, :-1] / tableau[:-1, :-1])

    # Check if the solution is unbounded or optimal
    if tableau[-1, min_ratio_index] < 0:
        print("The solution is unbounded.")
        break
    elif tableau[-1, -1] <= 0:
        print("The optimal solution is:", -tableau[:-1, -1])
        break

    # Pivot on the selected element
    pivot_row = np.argmin(tableau[min_ratio_index, :-1] / tableau[min_ratio_index, min_ratio_index])
    pivot_col = min_ratio_index
    tableau[pivot_row, :] /= tableau[pivot_row, pivot_col]
    tableau[:, pivot_col] /= tableau[pivot_row, pivot_col]
    tableau[:, :-1] -= tableau[pivot_row, :-1] * tableau[:, pivot_col][:, np.newaxis]
    tableau[:, -1] -= tableau[pivot_row, -1] * tableau[:, pivot_col][:, np.newaxis]

    # Update basic and non-basic variables
    basic[pivot_row], non_basic[pivot_col] = non_basic[pivot_col], basic[pivot_row]
