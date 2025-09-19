import heapq
from collections import defaultdict

def prim(graph, start=0):
    visited = set()
    mst = []
    total_weight = 0
    
    pq = [(0, start, -1)]
    
    while pq:
        weight, u, parent = heapq.heappop(pq)
        
        if u in visited:
            continue
        
        visited.add(u)
        if parent != -1:
            mst.append((parent, u, weight))
            total_weight += weight
        
        for v, w in graph[u]:
            if v not in visited:
                heapq.heappush(pq, (w, v, u))
    
    return mst, total_weight

def prim_matrix(matrix):
    n = len(matrix)
    visited = [False] * n
    key = [float('inf')] * n
    parent = [-1] * n
    
    key[0] = 0
    mst = []
    total_weight = 0
    
    for _ in range(n):
        min_key = float('inf')
        u = -1
        
        for v in range(n):
            if not visited[v] and key[v] < min_key:
                min_key = key[v]
                u = v
        
        visited[u] = True
        
        if parent[u] != -1:
            mst.append((parent[u], u, matrix[parent[u]][u]))
            total_weight += matrix[parent[u]][u]
        
        for v in range(n):
            if not visited[v] and matrix[u][v] < key[v]:
                key[v] = matrix[u][v]
                parent[v] = u
    
    return mst, total_weight

def prim_all_vertices(graph):
    if not graph:
        return [], 0
    
    vertices = set(graph.keys())
    for u in graph:
        for v, _ in graph[u]:
            vertices.add(v)
    
    if not vertices:
        return [], 0
    
    start = next(iter(vertices))
    return prim(graph, start)

def prim_with_validation(graph, n):
    mst, total_weight = prim(graph)
    
    if len(mst) != n - 1:
        return None, None
    
    return mst, total_weight