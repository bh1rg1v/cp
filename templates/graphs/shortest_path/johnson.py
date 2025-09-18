import heapq
from collections import defaultdict

def bellman_ford_johnson(graph, start, n):
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

def dijkstra_johnson(graph, start, h):
    dist = defaultdict(lambda: float('inf'))
    dist[start] = 0
    pq = [(0, start)]
    
    while pq:
        d, u = heapq.heappop(pq)
        
        if d > dist[u]:
            continue
            
        for v, w in graph[u]:
            new_weight = w + h[u] - h[v]
            if dist[u] + new_weight < dist[v]:
                dist[v] = dist[u] + new_weight
                heapq.heappush(pq, (dist[v], v))
    
    return dict(dist)

def johnson_all_pairs(graph, n):
    extended_graph = defaultdict(list)
    
    for u in graph:
        for v, w in graph[u]:
            extended_graph[u].append((v, w))
    
    for i in range(n):
        extended_graph[n].append((i, 0))
    
    h = bellman_ford_johnson(extended_graph, n, n + 1)
    
    if h is None:
        return None
    
    reweighted_graph = defaultdict(list)
    for u in graph:
        for v, w in graph[u]:
            new_weight = w + h[u] - h[v]
            reweighted_graph[u].append((v, new_weight))
    
    all_distances = {}
    
    for u in range(n):
        dist = dijkstra_johnson(reweighted_graph, u, h)
        
        original_dist = {}
        for v in dist:
            if dist[v] != float('inf'):
                original_dist[v] = dist[v] - h[u] + h[v]
            else:
                original_dist[v] = float('inf')
        
        all_distances[u] = original_dist
    
    return all_distances

def johnson_with_path(graph, n):
    extended_graph = defaultdict(list)
    
    for u in graph:
        for v, w in graph[u]:
            extended_graph[u].append((v, w))
    
    for i in range(n):
        extended_graph[n].append((i, 0))
    
    h = bellman_ford_johnson(extended_graph, n, n + 1)
    
    if h is None:
        return None, None
    
    reweighted_graph = defaultdict(list)
    for u in graph:
        for v, w in graph[u]:
            new_weight = w + h[u] - h[v]
            reweighted_graph[u].append((v, new_weight))
    
    all_distances = {}
    all_parents = {}
    
    for u in range(n):
        dist = defaultdict(lambda: float('inf'))
        parent = {}
        dist[u] = 0
        pq = [(0, u)]
        
        while pq:
            d, curr = heapq.heappop(pq)
            
            if d > dist[curr]:
                continue
                
            for v, w in reweighted_graph[curr]:
                if dist[curr] + w < dist[v]:
                    dist[v] = dist[curr] + w
                    parent[v] = curr
                    heapq.heappush(pq, (dist[v], v))
        
        original_dist = {}
        for v in dist:
            if dist[v] != float('inf'):
                original_dist[v] = dist[v] - h[u] + h[v]
            else:
                original_dist[v] = float('inf')
        
        all_distances[u] = original_dist
        all_parents[u] = parent
    
    return all_distances, all_parents

def reconstruct_path_johnson(parents, start, end):
    if end not in parents[start]:
        return []
    
    path = []
    current = end
    
    while current != start:
        path.append(current)
        current = parents[start][current]
    
    path.append(start)
    return path[::-1]

def johnson_sparse_optimized(edges, n):
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
    
    extended_edges = edges + [(n, i, 0) for i in range(n)]
    
    dist = [float('inf')] * (n + 1)
    dist[n] = 0
    
    for _ in range(n):
        for u, v, w in extended_edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    
    for u, v, w in extended_edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            return None
    
    h = dist[:n]
    
    all_distances = {}
    
    for start in range(n):
        dist = [float('inf')] * n
        dist[start] = 0
        pq = [(0, start)]
        
        while pq:
            d, u = heapq.heappop(pq)
            
            if d > dist[u]:
                continue
                
            for v, w in graph[u]:
                new_weight = w + h[u] - h[v]
                if dist[u] + new_weight < dist[v]:
                    dist[v] = dist[u] + new_weight
                    heapq.heappush(pq, (dist[v], v))
        
        original_dist = {}
        for v in range(n):
            if dist[v] != float('inf'):
                original_dist[v] = dist[v] - h[start] + h[v]
            else:
                original_dist[v] = float('inf')
        
        all_distances[start] = original_dist
    
    return all_distances