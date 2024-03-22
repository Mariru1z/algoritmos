def floyd_warshall(graph):
    # Número de vértices en el grafo
    n = len(graph)
    
    # Inicializar la matriz de distancias con valores infinitos
    dist = [[float('inf') for _ in range(n)] for _ in range(n)]

    # Llenar la matriz de distancias con los pesos del grafo
    for i in range(n):
        for j in range(n):
            if i == j:
                dist[i][j] = 0
            elif graph[i][j] != 0:
                dist[i][j] = graph[i][j]

    # Algoritmo Floyd-Warshall
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # Actualizar la distancia si se encuentra un camino más corto
                if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

# Ejemplo de uso con valores infinitos
graph = [
    [0, 9, float('inf'), 5, float('inf')],
    [9,0,5, float('inf'),8],
    [float('inf'),5,0,5,7],
    [5,float('inf'),5,0,7],
    [float('inf'),8,7,7,0]
]

result = floyd_warshall(graph)

# Imprimir la matriz de distancias
for row in result:
    print(row)

