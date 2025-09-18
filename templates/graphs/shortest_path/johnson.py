import heapq
from collections import defaultdict

def bellmanFord(graph, source, n):
    dist = [float('inf')] * n
    dist[source] = 0
    
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

def dijkstra(graph, source, h):
    dist = defaultdict(lambda: float('inf'))
    dist[source] = 0
    pq = [(0, source)]
    
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

def johnson(graph, n):
    extended_graph = defaultdict(list)
    
    for u in graph:
        for v, w in graph[u]:
            extended_graph[u].append((v, w))
    
    for i in range(n):
        extended_graph[n].append((i, 0))
    
    h = bellmanFord(extended_graph, n, n + 1)
    
    if h is None:
        return None
    
    reweighted_graph = defaultdict(list)
    for u in graph:
        for v, w in graph[u]:
            new_weight = w + h[u] - h[v]
            reweighted_graph[u].append((v, new_weight))
    
    all_distances = {}
    
    for u in range(n):
        dist = dijkstra(reweighted_graph, u, h)
        
        original_dist = {}
        for v in dist:
            if dist[v] != float('inf'):
                original_dist[v] = dist[v] - h[u] + h[v]
            else:
                original_dist[v] = float('inf')
        
        all_distances[u] = original_dist
    
    return all_distances