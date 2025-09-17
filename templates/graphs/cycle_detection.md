# Cycle Detection in Graphs

Cycle detection determines whether a graph contains cycles. Different algorithms are used for directed and undirected graphs.

## Algorithms

### Directed Graph - DFS with Colors
```python
def has_cycle_directed_dfs(graph, n):
    WHITE, GRAY, BLACK = 0, 1, 2
    color = [WHITE] * n
    
    def dfs(u):
        color[u] = GRAY  # Currently being processed
        
        for v in graph[u]:
            if color[v] == GRAY:  # Back edge found
                return True
            if color[v] == WHITE and dfs(v):
                return True
        
        color[u] = BLACK  # Finished processing
        return False
    
    for i in range(n):
        if color[i] == WHITE:
            if dfs(i):
                return True
    return False
```

### Directed Graph - Kahn's Algorithm
```python
def has_cycle_directed_kahn(graph, n):
    indegree = [0] * n
    
    for u in graph:
        for v in graph[u]:
            indegree[v] += 1
    
    queue = deque()
    for i in range(n):
        if indegree[i] == 0:
            queue.append(i)
    
    processed = 0
    while queue:
        u = queue.popleft()
        processed += 1
        
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)
    
    return processed != n  # Cycle exists if not all nodes processed
```

### Undirected Graph - DFS
```python
def has_cycle_undirected_dfs(graph, n):
    visited = [False] * n
    
    def dfs(u, parent):
        visited[u] = True
        
        for v in graph[u]:
            if not visited[v]:
                if dfs(v, u):
                    return True
            elif v != parent:  # Back edge to non-parent
                return True
        return False
    
    for i in range(n):
        if not visited[i]:
            if dfs(i, -1):
                return True
    return False
```

### Undirected Graph - Union-Find
```python
def has_cycle_undirected_union_find(edges, n):
    uf = UnionFind(n)
    
    for u, v in edges:
        if not uf.union(u, v):  # Already connected
            return True
    return False
```

## Complexity Analysis

| Algorithm | Graph Type | Time Complexity | Space Complexity |
|-----------|------------|----------------|------------------|
| **DFS (3-Color)** | Directed | **O(V + E)** | **O(V)** |
| **Kahn's Algorithm** | Directed | **O(V + E)** | **O(V)** |
| **DFS** | Undirected | **O(V + E)** | **O(V)** |
| **Union-Find** | Undirected | **O(E α(V))** | **O(V)** |

## Where & When to Use?

### ✅ Use Cycle Detection When:

#### Dependency Analysis
- **Build Systems**: Detect circular dependencies in compilation
- **Package Managers**: Prevent circular package dependencies
- **Task Scheduling**: Ensure no circular task dependencies
- **Database**: Detect circular foreign key references

#### Deadlock Detection
- **Operating Systems**: Detect resource allocation cycles
- **Database Transactions**: Prevent transaction deadlocks
- **Distributed Systems**: Detect distributed deadlocks
- **Concurrent Programming**: Analyze lock dependencies

#### Graph Validation
- **DAG Verification**: Ensure graph is acyclic for topological sorting
- **Tree Validation**: Verify tree structure (no cycles)
- **Workflow Validation**: Ensure process flows don't loop
- **State Machine**: Validate state transition graphs

#### Network Analysis
- **Routing Protocols**: Detect routing loops
- **Social Networks**: Find circular relationships
- **Supply Chain**: Detect circular dependencies
- **Communication**: Prevent message loops

### Algorithm Choice Guidelines:

#### For Directed Graphs:

**Use DFS (3-Color) When:**
- **Need actual cycle**: Want to find the cycle, not just detect
- **Recursive solution preferred**: Natural DFS implementation
- **Memory is not critical**: Recursion stack usage acceptable

**Use Kahn's Algorithm When:**
- **Iterative approach needed**: Avoid recursion stack limits
- **Topological sorting integration**: Part of larger topological sort
- **Level-by-level processing**: Natural BFS-like processing

#### For Undirected Graphs:

**Use DFS When:**
- **Simple implementation**: Straightforward recursive solution
- **Need cycle path**: Want to reconstruct the actual cycle
- **Adjacency list representation**: Natural traversal

**Use Union-Find When:**
- **Edge-by-edge processing**: Edges arrive incrementally
- **Dynamic connectivity**: Part of larger Union-Find application
- **Parallel processing**: Union-Find operations can be optimized

## Real-World Applications

### Software Engineering
- **Dependency Management**: Maven, npm, pip dependency resolution
- **Build Systems**: Make, Gradle circular dependency detection
- **Module Loading**: Prevent circular imports in programming languages
- **Code Analysis**: Static analysis for circular references

### Database Systems
- **Foreign Key Constraints**: Prevent circular references
- **Transaction Management**: Deadlock detection and prevention
- **Query Optimization**: Detect cycles in join graphs
- **Schema Validation**: Ensure referential integrity

### Operating Systems
- **Resource Allocation**: Banker's algorithm for deadlock prevention
- **Process Scheduling**: Detect circular wait conditions
- **Memory Management**: Detect circular references in garbage collection
- **File Systems**: Prevent circular symbolic links

### Network Protocols
- **Routing Protocols**: Prevent routing loops (BGP, OSPF)
- **Spanning Tree Protocol**: Eliminate loops in network topology
- **DNS Resolution**: Prevent circular DNS references
- **Load Balancing**: Avoid circular request forwarding

## Advanced Techniques

### Finding All Cycles
```python
def find_all_cycles_directed(graph, n):
    cycles = []
    WHITE, GRAY, BLACK = 0, 1, 2
    color = [WHITE] * n
    path = []
    
    def dfs(u):
        color[u] = GRAY
        path.append(u)
        
        for v in graph[u]:
            if color[v] == GRAY:
                # Found cycle
                cycle_start = path.index(v)
                cycles.append(path[cycle_start:] + [v])
            elif color[v] == WHITE:
                dfs(v)
        
        path.pop()
        color[u] = BLACK
    
    for i in range(n):
        if color[i] == WHITE:
            dfs(i)
    
    return cycles
```

### Cycle Detection with Path
```python
def find_cycle_with_path_directed(graph, n):
    WHITE, GRAY, BLACK = 0, 1, 2
    color = [WHITE] * n
    parent = [-1] * n
    
    def dfs(u):
        color[u] = GRAY
        
        for v in graph[u]:
            if color[v] == GRAY:
                # Reconstruct cycle
                cycle = []
                current = u
                while True:
                    cycle.append(current)
                    if current == v:
                        break
                    current = parent[current]
                return cycle[::-1]
            
            if color[v] == WHITE:
                parent[v] = u
                result = dfs(v)
                if result:
                    return result
        
        color[u] = BLACK
        return None
    
    for i in range(n):
        if color[i] == WHITE:
            cycle = dfs(i)
            if cycle:
                return cycle
    
    return None
```

### Minimum Cycle Detection
```python
def find_shortest_cycle_undirected(graph, n):
    min_cycle_length = float('inf')
    
    for start in range(n):
        dist = [-1] * n
        parent = [-1] * n
        queue = deque([start])
        dist[start] = 0
        
        while queue:
            u = queue.popleft()
            
            for v in graph[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    parent[v] = u
                    queue.append(v)
                elif parent[u] != v:
                    # Found cycle
                    cycle_length = dist[u] + dist[v] + 1
                    min_cycle_length = min(min_cycle_length, cycle_length)
    
    return min_cycle_length if min_cycle_length != float('inf') else -1
```

## Optimization Techniques

### Early Termination
```python
def has_cycle_early_termination(graph, n):
    visited = [False] * n
    rec_stack = [False] * n
    
    def dfs(u):
        visited[u] = True
        rec_stack[u] = True
        
        for v in graph[u]:
            if not visited[v]:
                if dfs(v):
                    return True
            elif rec_stack[v]:
                return True  # Early termination
        
        rec_stack[u] = False
        return False
    
    for i in range(n):
        if not visited[i]:
            if dfs(i):
                return True  # Early termination
    
    return False
```

### Memory Optimization
```python
def has_cycle_iterative_dfs(graph, n):
    visited = [False] * n
    
    for start in range(n):
        if visited[start]:
            continue
        
        stack = [(start, -1)]  # (node, parent)
        component_visited = set()
        
        while stack:
            u, parent = stack.pop()
            
            if u in component_visited:
                continue
            
            component_visited.add(u)
            visited[u] = True
            
            for v in graph[u]:
                if v == parent:
                    continue
                if v in component_visited:
                    return True
                stack.append((v, u))
    
    return False
```

## Common Patterns and Pitfalls

### Problem Recognition
Look for these keywords:
- **Circular dependencies**
- **Deadlock detection**
- **Loop prevention**
- **Acyclic verification**
- **Dependency resolution**

### Implementation Tips
1. **Choose appropriate algorithm** based on graph type and requirements
2. **Handle disconnected graphs** by checking all components
3. **Consider memory constraints** when choosing between recursive and iterative
4. **Early termination** can significantly improve performance

### Edge Cases
- **Self-loops**: Always create cycles
- **Empty graph**: No cycles
- **Single vertex**: No cycles (unless self-loop)
- **Tree**: No cycles by definition
- **Disconnected graph**: Check each component separately