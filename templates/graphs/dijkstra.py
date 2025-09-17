import heapq
from collections import defaultdict

def dijkstra(graph, start):
    dist = defaultdict(lambda: float('inf'))
    dist[start] = 0
    pq = [(0, start)]
    
    while pq:
        d, u = heapq.heappop(pq)
        
        if d > dist[u]:
            continue
            
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    
    return dict(dist)

def dijkstra_with_path(graph, start, end=None):
    dist = defaultdict(lambda: float('inf'))
    parent = {}
    dist[start] = 0
    pq = [(0, start)]
    
    while pq:
        d, u = heapq.heappop(pq)
        
        if d > dist[u]:
            continue
            
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u
                heapq.heappush(pq, (dist[v], v))
    
    path = []
    if end and end in parent:
        curr = end
        while curr != start:
            path.append(curr)
            curr = parent[curr]
        path.append(start)
        path.reverse()
    
    return dict(dist), path