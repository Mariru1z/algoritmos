# Get matrix dimensions from user
numero_filas = int(input("Enter number of rows: "))
nemro_columnas = int(input("Enter the of columns: "))
# Initialize the matrix
matrix = []

# Fill the matrix with user input
for i in range(numero_filas):
    row = []
    for j in range(nemro_columnas):
        value = int(input(f"Enter value for row {i+1}, column {j+1}: "))
        row.append(value)
    matrix.append(row)

# Print the matrix
for row in matrix:
    print(row)