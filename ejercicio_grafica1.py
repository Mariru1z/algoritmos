import math

# Estructura para representar un punto en el plano
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Definir el punto de referencia
referencePoint = None

# Función para encontrar el punto más abajo y más a la izquierda
def findBottomLeft(points):
    bottomLeft = 0
    for i in range(1, len(points)):
        if points[i].y < points[bottomLeft].y or \
           (points[i].y == points[bottomLeft].y and points[i].x < points[bottomLeft].x):
            bottomLeft = i
    return bottomLeft

# Función para calcular la orientación de tres puntos
def orientation(p, q, r):
    val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
    if val == 0:
        return 0  # colineales
    return 1 if val > 0 else 2  # en sentido horario o antihorario

# Función comparadora para ordenar los puntos por ángulo respecto al punto de referencia
def compare(p1, p2):
    o = orientation(referencePoint, p1, p2)
    if o == 0:
        return (p1.x - referencePoint.x) ** 2 + (p1.y - referencePoint.y) ** 2 < \
               (p2.x - referencePoint.x) ** 2 + (p2.y - referencePoint.y) ** 2
    return o == 2

# Función para encontrar la envolvente convexa utilizando el algoritmo Graham Scan
def convexHull(points):
    global referencePoint
    convexHullIndices = []

    # Encontrar el punto más abajo y a la izquierda como punto de referencia
    bottomLeft = findBottomLeft(points)
    referencePoint = points[bottomLeft]

    # Ordenar los puntos por ángulo respecto al punto de referencia
    sortedPoints = sorted(points, key=lambda p: (math.atan2(p.y - referencePoint.y, p.x - referencePoint.x),
                                                 p.x, p.y))

    # Iniciar el algoritmo Graham Scan
    s = []
    s.append(0)
    s.append(1)
    i = 2
    while i < len(sortedPoints):
        while len(s) >= 2:
            p1 = s.pop()
            p2 = s[-1]
            if orientation(sortedPoints[p2], sortedPoints[p1], sortedPoints[i]) == 2:
                s.append(p1)
                break
        s.append(i)
        i += 1

    # Extraer los índices de los puntos en la envolvente convexa
    while s:
        convexHullIndices.append(s.pop())

    return convexHullIndices

# datos
points = [Point(7, 6), Point(8, 4), Point(7, 2), Point(3, 2), Point(1, 6), Point(1, 8), Point(4, 9)]

convexHullIndices = convexHull(points)

# Imprimir los índices de la envolvente convexa
for idx in convexHullIndices:
    print(idx, end=" ")
print()
