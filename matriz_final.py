
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

    
    


