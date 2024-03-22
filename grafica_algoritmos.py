from scipy.spatial import ConvexHull

# Función para encontrar la envolvente convexa y devolver los índices de los puntos en sentido horario
def convex_hull_indices(points):
    # Calcular la envolvente convexa
    hull = ConvexHull(points)

    # Devolver los índices de los puntos en sentido horario
    return hull.vertices.tolist()

# Ejemplo de uso
points = [[7, 6], [8, 4], [7, 2], [3, 2], [1, 6], [1, 8], [4, 9]]
convex_hull_indices = convex_hull_indices(points)
print(convex_hull_indices)
