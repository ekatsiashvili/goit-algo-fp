import heapq

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, name):
        self.vertices[name] = {}

    def add_edge(self, src, dest, weight):
        self.vertices[src][dest] = weight

    def dijkstra(self, start):
        distances = {vertex: float('infinity') for vertex in self.vertices}
        distances[start] = 0
        heap = [(0, start)]

        while heap:
            current_distance, current_vertex = heapq.heappop(heap)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.vertices[current_vertex].items():
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(heap, (distance, neighbor))

        return distances

# Test
g = Graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')
g.add_vertex('E')

g.add_edge('A', 'B', 6)
g.add_edge('A', 'D', 1)
g.add_edge('D', 'B', 2)
g.add_edge('D', 'E', 1)
g.add_edge('D', 'C', 2)
g.add_edge('C', 'B', 5)
g.add_edge('E', 'B', 2)

distances_from_a = g.dijkstra('A')
print(distances_from_a)
