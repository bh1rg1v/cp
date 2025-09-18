# Strongly Connected Components (SCCs)

A strongly connected component is a maximal set of vertices in a directed graph where every vertex is reachable from every other vertex within the component.

## Algorithms

### Kosaraju's Algorithm
```python
def kosaraju_scc(graph, n):
    visited = [False] * n
    stack = []
    
    # First DFS: fill stack with finish times
    def dfs1(u):
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                dfs1(v)
        stack.append(u)
    
    for i in range(n):
        if not visited[i]:
            dfs1(i)
    
    # Create transpose graph
    transpose = defaultdict(list)
    for u in graph:
        for v in graph[u]:
            transpose[v].append(u)
    
    # Second DFS on transpose graph
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
```

### Tarjan's Algorithm
```python
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
```

### Tarjan's Bridge-Finding Algorithm
```python
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
                
                if low[v] > disc[u]:  # Bridge condition
                    bridges.append((u, v))
            elif v != parent[u]:
                low[u] = min(low[u], disc[v])
    
    for i in range(n):
        if not visited[i]:
            bridge_dfs(i)
    
    return bridges
```

### Tarjan's Articulation Points Algorithm
```python
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
                
                # Root is articulation point if it has > 1 children
                if parent[u] == -1 and children > 1:
                    ap[u] = True
                
                # Non-root is articulation point if low[v] >= disc[u]
                if parent[u] != -1 and low[v] >= disc[u]:
                    ap[u] = True
            elif v != parent[u]:
                low[u] = min(low[u], disc[v])
    
    for i in range(n):
        if not visited[i]:
            ap_dfs(i)
    
    return [i for i in range(n) if ap[i]]
```

## Complexity Analysis

| Algorithm | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| **Kosaraju's** | **O(V + E)** | **O(V + E)** |
| **Tarjan's SCC** | **O(V + E)** | **O(V)** |
| **Tarjan's Bridges** | **O(V + E)** | **O(V)** |
| **Tarjan's Articulation Points** | **O(V + E)** | **O(V)** |

## Where & When to Use?

### ✅ Use SCC Algorithms When:

#### Graph Analysis
- **Web Graph Analysis**: Identify strongly connected web page clusters
- **Social Network Analysis**: Find tightly connected user groups
- **Citation Networks**: Identify mutually citing paper clusters
- **Dependency Analysis**: Find circular dependency groups

#### System Design
- **Distributed Systems**: Identify communication clusters
- **Database Design**: Optimize query execution plans
- **Compiler Optimization**: Identify strongly connected code regions
- **Network Topology**: Analyze network robustness

#### Algorithmic Problems
- **2-SAT Problem**: Solve satisfiability using SCC decomposition
- **Graph Condensation**: Create DAG from directed graph
- **Reachability Queries**: Preprocess for fast reachability tests
- **Shortest Path Optimization**: Optimize paths within SCCs

### ✅ Use Bridge/Articulation Point Algorithms When:

#### Network Reliability
- **Network Design**: Identify critical connections/nodes
- **Fault Tolerance**: Find single points of failure
- **Infrastructure Planning**: Ensure network redundancy
- **Communication Networks**: Identify critical links

#### Graph Connectivity
- **Bridge Networks**: Find connections between components
- **Cut Vertices**: Identify vertices whose removal disconnects graph
- **Network Vulnerability**: Assess network robustness
- **Spanning Tree**: Optimize tree construction

### Algorithm Choice Guidelines:

#### Use Kosaraju's When:
- **Simple implementation preferred**: Easier to understand and implement
- **Educational purposes**: Good for learning SCC concepts
- **Transpose graph is useful**: Need reverse graph for other purposes
- **Two-pass approach acceptable**: Don't mind running DFS twice

#### Use Tarjan's When:
- **Single-pass efficiency**: Want to find SCCs in one traversal
- **Memory efficiency**: Don't want to store transpose graph
- **Online algorithm**: Process vertices as they're discovered
- **Production systems**: Generally more efficient in practice

## Real-World Applications

### Web and Internet
- **PageRank Algorithm**: Identify strongly connected web communities
- **Web Crawling**: Optimize crawling strategies for connected regions
- **Link Analysis**: Find mutually linking website clusters
- **Search Engine Optimization**: Analyze link structure

### Social Networks
- **Community Detection**: Find tightly connected user groups
- **Influence Analysis**: Identify influential user clusters
- **Recommendation Systems**: Group users with similar connections
- **Viral Marketing**: Target strongly connected communities

### Software Engineering
- **Call Graph Analysis**: Identify mutually recursive function groups
- **Module Dependencies**: Find circular dependency clusters
- **Code Refactoring**: Identify tightly coupled code regions
- **Static Analysis**: Detect problematic code structures

### Transportation and Logistics
- **Route Planning**: Identify strongly connected road networks
- **Public Transportation**: Optimize transit system design
- **Supply Chain**: Analyze circular dependencies in supply networks
- **Traffic Flow**: Identify critical intersections and roads

## Advanced Applications

### 2-SAT Problem Solution
```python
def solve_2sat(clauses, n):
    # Build implication graph
    graph = defaultdict(list)
    
    for a, b in clauses:  # (a OR b) clause
        # NOT a => b, NOT b => a
        graph[a ^ 1].append(b)
        graph[b ^ 1].append(a)
    
    # Find SCCs
    sccs = tarjan_scc(graph, 2 * n)
    
    # Check if variable and its negation are in same SCC
    scc_id = [-1] * (2 * n)
    for i, scc in enumerate(sccs):
        for node in scc:
            scc_id[node] = i
    
    for i in range(n):
        if scc_id[2 * i] == scc_id[2 * i + 1]:
            return None  # Unsatisfiable
    
    # Construct solution
    assignment = [False] * n
    for i in range(n):
        assignment[i] = scc_id[2 * i] > scc_id[2 * i + 1]
    
    return assignment
```

### Graph Condensation
```python
def condensation_graph(graph, n):
    sccs = tarjan_scc(graph, n)
    scc_id = [-1] * n
    
    for i, scc in enumerate(sccs):
        for node in scc:
            scc_id[node] = i
    
    # Build condensed DAG
    condensed = defaultdict(set)
    for u in graph:
        for v in graph[u]:
            if scc_id[u] != scc_id[v]:
                condensed[scc_id[u]].add(scc_id[v])
    
    return condensed, sccs
```

### Critical Path Analysis
```python
def find_critical_edges(graph, n):
    bridges = tarjan_bridges(graph, n)
    articulation_points = tarjan_articulation_points(graph, n)
    
    return {
        'critical_edges': bridges,
        'critical_vertices': articulation_points
    }
```

## Optimization Techniques

### Path Compression in Tarjan's
```python
def tarjan_scc_optimized(graph, n):
    # Use path compression for better performance
    index_counter = [0]
    stack = []
    lowlinks = [-1] * n
    index = [-1] * n
    on_stack = [False] * n
    sccs = []
    
    def strongconnect(u):
        index[u] = lowlinks[u] = index_counter[0]
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
```

### Iterative Implementation
```python
def kosaraju_iterative(graph, n):
    # Iterative version to avoid stack overflow
    visited = [False] * n
    finish_order = []
    
    # First DFS iteratively
    for start in range(n):
        if visited[start]:
            continue
        
        stack = [start]
        path = []
        
        while stack:
            u = stack[-1]
            
            if not visited[u]:
                visited[u] = True
                path.append(u)
            
            found_unvisited = False
            for v in graph[u]:
                if not visited[v]:
                    stack.append(v)
                    found_unvisited = True
                    break
            
            if not found_unvisited:
                stack.pop()
                if path and path[-1] == u:
                    finish_order.append(path.pop())
    
    # Build transpose and run second DFS
    transpose = defaultdict(list)
    for u in graph:
        for v in graph[u]:
            transpose[v].append(u)
    
    visited = [False] * n
    sccs = []
    
    for start in reversed(finish_order):
        if visited[start]:
            continue
        
        component = []
        stack = [start]
        
        while stack:
            u = stack.pop()
            if not visited[u]:
                visited[u] = True
                component.append(u)
                for v in transpose[u]:
                    if not visited[v]:
                        stack.append(v)
        
        if component:
            sccs.append(component)
    
    return sccs
```

## Common Patterns and Applications

### Problem Recognition
Look for these keywords:
- **Strongly connected**
- **Mutual reachability**
- **Circular dependencies**
- **Critical connections**
- **Bridge/Cut vertex**
- **Network reliability**

### Implementation Tips
1. **Choose appropriate algorithm** based on requirements and constraints
2. **Handle disconnected graphs** by processing all components
3. **Consider iterative versions** for very large graphs to avoid stack overflow
4. **Use appropriate data structures** for graph representation

### Edge Cases
- **Self-loops**: Each vertex with self-loop forms its own SCC
- **Empty graph**: Each vertex is its own SCC
- **Tree**: Each vertex is its own SCC, all edges are bridges
- **Complete graph**: Entire graph is one SCC, no bridges
- **Disconnected graph**: Process each component separately