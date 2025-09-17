def floyd_warshall(graph, n):
    dist = [[float('inf')] * n for _ in range(n)]
    
    for i in range(n):
        dist[i][i] = 0
    
    for u in graph:
        for v, w in graph[u]:
            dist[u][v] = min(dist[u][v], w)
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist

def floyd_warshall_with_path(graph, n):
    dist = [[float('inf')] * n for _ in range(n)]
    next_node = [[-1] * n for _ in range(n)]
    
    for i in range(n):
        dist[i][i] = 0
    
    for u in graph:
        for v, w in graph[u]:
            if w < dist[u][v]:
                dist[u][v] = w
                next_node[u][v] = v
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        next_node[i][j] = next_node[i][k]
    
    return dist, next_node

def reconstruct_path(next_node, start, end):
    if next_node[start][end] == -1:
        return []
    
    path = [start]
    current = start
    
    while current != end:
        current = next_node[current][end]
        path.append(current)
    
    return path

def has_negative_cycle_floyd(dist, n):
    for i in range(n):
        if dist[i][i] < 0:
            return True
    return False

def floyd_warshall_matrix(adj_matrix):
    n = len(adj_matrix)
    dist = [row[:] for row in adj_matrix]
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist