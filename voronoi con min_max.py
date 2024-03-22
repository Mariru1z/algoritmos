#voronoi con min_max
import numpy as np
import matplotlib.pyplot as plt

# Definir los puntos de semilla (sitios)
seed_points = np.array([[1, 2], [3, 4], [5, 6],[3, 3]])

# Definir el área de interés
x_min, x_max = 0, 8
y_min, y_max = 0, 8

# Generar una malla de puntos en el área de interés
x_range = np.arange(x_min, x_max, 0.1)
y_range = np.arange(y_min, y_max, 0.1)
xx, yy = np.meshgrid(x_range, y_range)
points_of_interest = np.c_[xx.ravel(), yy.ravel()]

# Función para calcular la celda de Voronoi de un punto
def voronoi_cell(point, seed_points):
    distances = np.linalg.norm(seed_points - point, axis=1)
    return np.argmin(distances)

# Calcular la celda de Voronoi para cada punto de interés
voronoi_map = np.array([voronoi_cell(point, seed_points) for point in points_of_interest])

# Visualizar el diagrama de Voronoi
plt.scatter(points_of_interest[:, 0], points_of_interest[:, 1], c=voronoi_map, cmap='viridis', marker='.')
plt.scatter(seed_points[:, 0], seed_points[:, 1], c='red', marker='o', label='Puntos')
plt.legend()
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.gca().set_aspect('equal', adjustable='box')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Voronoi')
plt.grid(True)
plt.show()