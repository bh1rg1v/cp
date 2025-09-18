from collections import deque, defaultdict

def is_bipartite_bfs(graph):
    color = {}
    
    for start in graph:
        if start in color:
            continue
            
        queue = deque([start])
        color[start] = 0
        
        while queue:
            u = queue.popleft()
            
            for v in graph[u]:
                if v not in color:
                    color[v] = 1 - color[u]
                    queue.append(v)
                elif color[v] == color[u]:
                    return False
    
    return True

def is_bipartite_dfs(graph):
    color = {}
    
    def dfs(u, c):
        color[u] = c
        
        for v in graph[u]:
            if v not in color:
                if not dfs(v, 1 - c):
                    return False
            elif color[v] == color[u]:
                return False
        
        return True
    
    for start in graph:
        if start not in color:
            if not dfs(start, 0):
                return False
    
    return True

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True

def is_bipartite_union_find(edges, n):
    uf = UnionFind(2 * n)
    
    for u, v in edges:
        if uf.find(u) == uf.find(v) or uf.find(u + n) == uf.find(v + n):
            return False
        uf.union(u, v + n)
        uf.union(u + n, v)
    
    return True