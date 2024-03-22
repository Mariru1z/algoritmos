# proporcionar las dimensiones
numero_filas = int(input("numero de filas: "))
nemro_columnas = int(input("numero de columnas: "))
# Inicia la matriz
matrix = []

# matriz dada por el usuario
for i in range(numero_filas):
    row = []
    for j in range(nemro_columnas):
        value = int(input(f"valor de la fila {i+1}, valor de la columna {j+1}: "))
        row.append(value)
    matrix.append(row)

# matriz3
for row in matrix:
    print(row)