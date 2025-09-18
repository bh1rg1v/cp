from collections import defaultdict, deque

def has_cycle_directed_dfs(graph, n):
    WHITE, GRAY, BLACK = 0, 1, 2
    color = [WHITE] * n
    
    def dfs(u):
        color[u] = GRAY
        
        for v in graph[u]:
            if color[v] == GRAY:
                return True
            if color[v] == WHITE and dfs(v):
                return True
        
        color[u] = BLACK
        return False
    
    for i in range(n):
        if color[i] == WHITE:
            if dfs(i):
                return True
    
    return False

def has_cycle_directed_kahn(graph, n):
    indegree = [0] * n
    
    for u in graph:
        for v in graph[u]:
            indegree[v] += 1
    
    queue = deque()
    for i in range(n):
        if indegree[i] == 0:
            queue.append(i)
    
    processed = 0
    
    while queue:
        u = queue.popleft()
        processed += 1
        
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)
    
    return processed != n

def has_cycle_undirected_dfs(graph, n):
    visited = [False] * n
    
    def dfs(u, parent):
        visited[u] = True
        
        for v in graph[u]:
            if not visited[v]:
                if dfs(v, u):
                    return True
            elif v != parent:
                return True
        
        return False
    
    for i in range(n):
        if not visited[i]:
            if dfs(i, -1):
                return True
    
    return False

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

def has_cycle_undirected_union_find(edges, n):
    uf = UnionFind(n)
    
    for u, v in edges:
        if not uf.union(u, v):
            return True
    
    return False

def find_cycle_directed_dfs(graph, n):
    WHITE, GRAY, BLACK = 0, 1, 2
    color = [WHITE] * n
    parent = [-1] * n
    cycle = []
    
    def dfs(u):
        color[u] = GRAY
        
        for v in graph[u]:
            if color[v] == GRAY:
                cycle_start = v
                current = u
                cycle.append(cycle_start)
                
                while current != cycle_start:
                    cycle.append(current)
                    current = parent[current]
                
                return True
            
            if color[v] == WHITE:
                parent[v] = u
                if dfs(v):
                    return True
        
        color[u] = BLACK
        return False
    
    for i in range(n):
        if color[i] == WHITE:
            if dfs(i):
                return cycle[::-1]
    
    return []

def find_cycle_undirected_dfs(graph, n):
    visited = [False] * n
    parent = [-1] * n
    
    def dfs(u, p):
        visited[u] = True
        parent[u] = p
        
        for v in graph[u]:
            if not visited[v]:
                cycle = dfs(v, u)
                if cycle:
                    return cycle
            elif v != p:
                cycle = []
                current = u
                while current != v:
                    cycle.append(current)
                    current = parent[current]
                cycle.append(v)
                return cycle
        
        return []
    
    for i in range(n):
        if not visited[i]:
            cycle = dfs(i, -1)
            if cycle:
                return cycle
    
    return []