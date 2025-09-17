import heapq
from collections import defaultdict

def dijkstra(graph, start):
    """
    Dijkstra's shortest path algorithm
    
    Args:
        graph: dict of adjacency lists {node: [(neighbor, weight), ...]}
        start: starting node
    
    Returns:
        dict: {node: shortest_distance_from_start}
    """
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
    """
    Dijkstra with path reconstruction
    
    Returns:
        tuple: (distances_dict, path_to_end_if_specified)
    """
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

# Example usage
if __name__ == "__main__":
    # Graph representation: {node: [(neighbor, weight), ...]}
    graph = {
        0: [(1, 4), (2, 1)],
        1: [(3, 1)],
        2: [(1, 2), (3, 5)],
        3: []
    }
    
    distances = dijkstra(graph, 0)
    print("Shortest distances from node 0:", distances)
    
    distances, path = dijkstra_with_path(graph, 0, 3)
    print("Path from 0 to 3:", path)