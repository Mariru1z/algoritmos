import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d

# Generamos un conjunto de puntos aleatorios en el plano
np.random.seed(0)
points = np.random.rand(10, 2)  # 10 puntos en el plano 2D

# Calculamos el diagrama de Voronoi
vor = Voronoi(points)

# Visualizamos el diagrama de Voronoi
voronoi_plot_2d(vor)
plt.plot(points[:, 0], points[:, 1], 'ko')  # Plot de los puntos de entrada
plt.show()
