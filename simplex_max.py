import numpy as np


#Para facilitar la resolución emplearemos la librería NumPy
"""
NumPy
Es una biblioteca para el lenguaje de programación Python que da soporte
para crear vectores y matrices grandes multidimensionales, junto con una
gran colección de funciones matemáticas de alto nivel para operar con ellas.
"""

def metodo_simplex(A, b, c):
    """
    Implementa el método simplex para resolver problemas de maximización.

    Parámetros:
    - A: matriz de coeficientes de las restricciones.
    - b: vector de términos constantes de las restricciones.
    - c: vector de coeficientes de la función objetivo.

    La función retorna la solución óptima y el valor máximo.
    """

    # Paso 1: Inicialización
    num_vars = len(c)

    # Forma la tabla simplex inicial con A, b, c y variables de holgura.
    nun_holgura_vars = len(b)

    #print(nun_holgura_vars)

    tabla_simplex = np.hstack((A, np.eye(nun_holgura_vars), b.reshape(-1, 1)))
    tabla_simplex = np.vstack((tabla_simplex, np.hstack((-c, np.zeros(nun_holgura_vars + 1)))))

    while True:
        # Paso 2: Comprobación de la condición de optimalidad
        if np.all(tabla_simplex[-1, :-1] >= 0):
            print("Se ha encontrado una solución óptima.")
            break

        # Paso 3: Variable entrante (columna del pivote)
        pivot_col = np.argmin(tabla_simplex[-1, :-1])

        # Paso 4: Variable saliente (fila del pivote)
        proporcion = tabla_simplex[:-1, -1] / tabla_simplex[:-1, pivot_col]
        pivot_reng = np.argwhere(proporcion == np.min(proporcion[np.where(proporcion > 0)]))[0][0]

        # Paso 5: Pivoteo
        tabla_simplex = pivot_operation(tabla_simplex, pivot_reng, pivot_col)

        # Muestra la tabla simplex actual
        print("Iteración actual:")
        print(tabla_simplex)

    # Extrae la solución óptima y el valor de la función objetivo
    v_solucion = tabla_simplex[:-1, -1]
    valor_objetivo = -tabla_simplex[-1, -1]
    return v_solucion, valor_objetivo

def pivot_operation(tabla_simplex, pivot_reng, pivot_col):
    """
    Realiza la operación de pivote en la tabla simplex.
    """
    # Normaliza la fila del pivote
    tabla_simplex[pivot_reng, :] /= tabla_simplex[pivot_reng, pivot_col]
    for i in range(len(tabla_simplex)):
        if i != pivot_reng:
            tabla_simplex[i, :] -= tabla_simplex[i, pivot_col] * tabla_simplex[pivot_reng, :]
    return tabla_simplex



# Ejemplo de uso A
A = np.array([[1, 2], [4, 0], [0, 4]])
b = np.array([8, 16, 12])
c = np.array([1, 1])


solucion, valor = metodo_simplex(A, b, c)

print(10*"------")
print("Solución óptima:", solucion)
print("Valor de la función objetivo:", valor)
print(10*"------")


"""
Elementos de Programación Lineal 
Maximización 
Taha Hamdy 
"""