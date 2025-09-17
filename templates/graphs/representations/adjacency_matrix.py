class AdjacencyMatrix:
    def __init__(self, num_vertices, directed=False):
        self.num_vertices = num_vertices
        self.directed = directed
        self.matrix = [[0] * num_vertices for _ in range(num_vertices)]
    
    def add_edge(self, u, v, weight=1):
        if 0 <= u < self.num_vertices and 0 <= v < self.num_vertices:
            self.matrix[u][v] = weight
            if not self.directed:
                self.matrix[v][u] = weight
    
    def remove_edge(self, u, v):
        if 0 <= u < self.num_vertices and 0 <= v < self.num_vertices:
            self.matrix[u][v] = 0
            if not self.directed:
                self.matrix[v][u] = 0
    
    def get_neighbors(self, u):
        if 0 <= u < self.num_vertices:
            return [(v, self.matrix[u][v]) for v in range(self.num_vertices) 
                    if self.matrix[u][v] != 0]
        return []
    
    def has_edge(self, u, v):
        if 0 <= u < self.num_vertices and 0 <= v < self.num_vertices:
            return self.matrix[u][v] != 0
        return False
    
    def get_weight(self, u, v):
        if 0 <= u < self.num_vertices and 0 <= v < self.num_vertices:
            return self.matrix[u][v]
        return 0
    
    def print_matrix(self):
        for row in self.matrix:
            print(row)