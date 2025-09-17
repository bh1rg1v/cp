from collections import defaultdict

class AdjacencyList:
    def __init__(self, directed=False):
        self.graph = defaultdict(list)
        self.directed = directed
    
    def add_edge(self, u, v, weight=1):
        self.graph[u].append((v, weight))
        if not self.directed:
            self.graph[v].append((u, weight))
    
    def remove_edge(self, u, v):
        self.graph[u] = [(node, w) for node, w in self.graph[u] if node != v]
        if not self.directed:
            self.graph[v] = [(node, w) for node, w in self.graph[v] if node != u]
    
    def get_neighbors(self, u):
        return self.graph[u]
    
    def has_edge(self, u, v):
        return any(node == v for node, _ in self.graph[u])
    
    def get_vertices(self):
        vertices = set(self.graph.keys())
        for neighbors in self.graph.values():
            vertices.update(node for node, _ in neighbors)
        return list(vertices)
    
    def print_graph(self):
        for vertex in sorted(self.graph.keys()):
            neighbors = [f"{v}({w})" for v, w in self.graph[vertex]]
            print(f"{vertex}: {neighbors}")