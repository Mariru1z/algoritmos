import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Ejemplo de uso
graph = {
    'A': [('D', 5), ('B', 2)],
    'B': [('C', 3), ('E', 2)],
    'C': [('Z', 7)],
    'D': [('F', 6), ('E', 1)],
    'E': [('H', 5), ('G', 2)],
    'F': [('Z', 5)],
    'G': [('Z', 3)],
    'H': [('I', 4)],
    'I': [('Z', 1)],
    'Z': []
}

start_node = 'A'
result = dijkstra(graph, start_node)

# Imprimir las distancias más cortas desde el nodo de inicio
for node, distance in result.items():
    print(f"De {start_node} a -> {node}: {distance}")
