from collections import deque, defaultdict

def topological_sort_kahn(graph, n):
    indegree = [0] * n
    
    for u in graph:
        for v in graph[u]:
            indegree[v] += 1
    
    queue = deque()
    for i in range(n):
        if indegree[i] == 0:
            queue.append(i)
    
    result = []
    
    while queue:
        u = queue.popleft()
        result.append(u)
        
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)
    
    return result if len(result) == n else []

def topological_sort_dfs(graph, n):
    visited = [False] * n
    stack = []
    
    def dfs(u):
        visited[u] = True
        
        for v in graph[u]:
            if not visited[v]:
                dfs(v)
        
        stack.append(u)
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
    
    return stack[::-1]

def has_cycle_dfs(graph, n):
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

def topological_sort_with_cycle_check(graph, n):
    if has_cycle_dfs(graph, n):
        return []
    return topological_sort_dfs(graph, n)