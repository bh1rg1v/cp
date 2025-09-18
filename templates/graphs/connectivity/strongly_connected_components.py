from collections import defaultdict

def kosaraju_scc(graph, n):
    visited = [False] * n
    stack = []
    
    def dfs1(u):
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                dfs1(v)
        stack.append(u)
    
    for i in range(n):
        if not visited[i]:
            dfs1(i)
    
    transpose = defaultdict(list)
    for u in graph:
        for v in graph[u]:
            transpose[v].append(u)
    
    visited = [False] * n
    sccs = []
    
    def dfs2(u, component):
        visited[u] = True
        component.append(u)
        for v in transpose[u]:
            if not visited[v]:
                dfs2(v, component)
    
    while stack:
        u = stack.pop()
        if not visited[u]:
            component = []
            dfs2(u, component)
            sccs.append(component)
    
    return sccs

def tarjan_scc(graph, n):
    index_counter = [0]
    stack = []
    lowlinks = [-1] * n
    index = [-1] * n
    on_stack = [False] * n
    sccs = []
    
    def strongconnect(u):
        index[u] = index_counter[0]
        lowlinks[u] = index_counter[0]
        index_counter[0] += 1
        stack.append(u)
        on_stack[u] = True
        
        for v in graph[u]:
            if index[v] == -1:
                strongconnect(v)
                lowlinks[u] = min(lowlinks[u], lowlinks[v])
            elif on_stack[v]:
                lowlinks[u] = min(lowlinks[u], index[v])
        
        if lowlinks[u] == index[u]:
            component = []
            while True:
                w = stack.pop()
                on_stack[w] = False
                component.append(w)
                if w == u:
                    break
            sccs.append(component)
    
    for u in range(n):
        if index[u] == -1:
            strongconnect(u)
    
    return sccs

def tarjan_bridges(graph, n):
    time = [0]
    visited = [False] * n
    disc = [-1] * n
    low = [-1] * n
    parent = [-1] * n
    bridges = []
    
    def bridge_dfs(u):
        visited[u] = True
        disc[u] = low[u] = time[0]
        time[0] += 1
        
        for v in graph[u]:
            if not visited[v]:
                parent[v] = u
                bridge_dfs(v)
                
                low[u] = min(low[u], low[v])
                
                if low[v] > disc[u]:
                    bridges.append((u, v))
            
            elif v != parent[u]:
                low[u] = min(low[u], disc[v])
    
    for i in range(n):
        if not visited[i]:
            bridge_dfs(i)
    
    return bridges

def tarjan_articulation_points(graph, n):
    time = [0]
    visited = [False] * n
    disc = [-1] * n
    low = [-1] * n
    parent = [-1] * n
    ap = [False] * n
    
    def ap_dfs(u):
        children = 0
        visited[u] = True
        disc[u] = low[u] = time[0]
        time[0] += 1
        
        for v in graph[u]:
            if not visited[v]:
                children += 1
                parent[v] = u
                ap_dfs(v)
                
                low[u] = min(low[u], low[v])
                
                if parent[u] == -1 and children > 1:
                    ap[u] = True
                
                if parent[u] != -1 and low[v] >= disc[u]:
                    ap[u] = True
            
            elif v != parent[u]:
                low[u] = min(low[u], disc[v])
    
    for i in range(n):
        if not visited[i]:
            ap_dfs(i)
    
    return [i for i in range(n) if ap[i]]

def is_strongly_connected(graph, n):
    sccs = kosaraju_scc(graph, n)
    return len(sccs) == 1

def condensation_graph(graph, n):
    sccs = tarjan_scc(graph, n)
    scc_id = [-1] * n
    
    for i, scc in enumerate(sccs):
        for node in scc:
            scc_id[node] = i
    
    condensed = defaultdict(set)
    
    for u in graph:
        for v in graph[u]:
            if scc_id[u] != scc_id[v]:
                condensed[scc_id[u]].add(scc_id[v])
    
    return condensed, sccs