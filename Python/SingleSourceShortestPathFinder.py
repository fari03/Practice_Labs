import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))

    def dijkstra(self, source):
        distances = [float('inf')] * self.V
        distances[source] = 0

        heap = [(0, source)]

        while heap:
            dist, u = heapq.heappop(heap)

            if dist > distances[u]:
                continue

            for v, w in self.graph[u]:
                new_dist = distances[u] + w

                if new_dist < distances[v]:
                    distances[v] = new_dist
                    heapq.heappush(heap, (new_dist, v))

        return distances


# Example usage
g = Graph(5)
g.add_edge(0, 1, 2)
g.add_edge(0, 3, 6)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 8)
g.add_edge(1, 4, 5)
g.add_edge(2, 4, 7)
g.add_edge(3, 4, 9)

source = 0
distances = g.dijkstra(source)

print("Vertex\tDistance from Source")
for v in range(g.V):
    print(f"{v}\t{distances[v]}")
