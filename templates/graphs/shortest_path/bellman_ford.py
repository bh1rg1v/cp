from collections import defaultdict

def bellman_ford(graph, start, n):
    dist = [float('inf')] * n
    dist[start] = 0
    
    for _ in range(n - 1):
        for u in graph:
            if dist[u] != float('inf'):
                for v, w in graph[u]:
                    if dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
    
    for u in graph:
        if dist[u] != float('inf'):
            for v, w in graph[u]:
                if dist[u] + w < dist[v]:
                    return None
    
    return dist

def bellman_ford_with_path(graph, start, n):
    dist = [float('inf')] * n
    parent = [-1] * n
    dist[start] = 0
    
    for _ in range(n - 1):
        for u in graph:
            if dist[u] != float('inf'):
                for v, w in graph[u]:
                    if dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
                        parent[v] = u
    
    for u in graph:
        if dist[u] != float('inf'):
            for v, w in graph[u]:
                if dist[u] + w < dist[v]:
                    return None, None
    
    return dist, parent

def detect_negative_cycle(graph, n):
    dist = [0] * n
    
    for _ in range(n - 1):
        for u in graph:
            for v, w in graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
    
    for u in graph:
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                return True
    
    return False

def bellman_ford_edges(edges, start, n):
    dist = [float('inf')] * n
    dist[start] = 0
    
    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            return None
    
    return dist