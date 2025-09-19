# Prim's Algorithm

Prim's algorithm finds a minimum spanning tree (MST) of a connected, undirected graph using a greedy approach that grows the MST one vertex at a time.

## Algorithm Overview

Prim's algorithm works by:
1. **Start with any vertex** as the initial MST
2. **Repeatedly add the minimum weight edge** that connects the MST to a new vertex
3. **Continue until all vertices** are included in the MST

## Implementation

### Heap-Based Prim's (Recommended)
```python
def prim(graph, start=0):
    visited = set()
    mst = []
    total_weight = 0
    
    pq = [(0, start, -1)]  # (weight, vertex, parent)
    
    while pq:
        weight, u, parent = heapq.heappop(pq)
        
        if u in visited:
            continue
        
        visited.add(u)
        if parent != -1:
            mst.append((parent, u, weight))
            total_weight += weight
        
        # Add all edges from u to unvisited vertices
        for v, w in graph[u]:
            if v not in visited:
                heapq.heappush(pq, (w, v, u))
    
    return mst, total_weight
```

### Matrix-Based Prim's
```python
def prim_matrix(matrix):
    n = len(matrix)
    visited = [False] * n
    key = [float('inf')] * n  # Minimum weight to connect to MST
    parent = [-1] * n
    
    key[0] = 0  # Start from vertex 0
    mst = []
    total_weight = 0
    
    for _ in range(n):
        # Find minimum key vertex not yet in MST
        min_key = float('inf')
        u = -1
        for v in range(n):
            if not visited[v] and key[v] < min_key:
                min_key = key[v]
                u = v
        
        visited[u] = True
        
        # Add edge to MST (except for first vertex)
        if parent[u] != -1:
            mst.append((parent[u], u, matrix[parent[u]][u]))
            total_weight += matrix[parent[u]][u]
        
        # Update key values of adjacent vertices
        for v in range(n):
            if not visited[v] and matrix[u][v] < key[v]:
                key[v] = matrix[u][v]
                parent[v] = u
    
    return mst, total_weight
```

### With Connectivity Validation
```python
def prim_with_validation(graph, n):
    mst, total_weight = prim(graph)
    
    if len(mst) != n - 1:
        return None, None  # Graph is not connected
    
    return mst, total_weight
```

## Complexity Analysis

| Implementation | Time Complexity | Space Complexity |
|----------------|----------------|------------------|
| **Heap-Based** | **O(E log V)** | **O(V)** |
| **Matrix-Based** | **O(V²)** | **O(V)** |
| **Fibonacci Heap** | **O(E + V log V)** | **O(V)** |

## Where & When to Use?

### ✅ Use Prim's Algorithm When:

#### Dense Graphs
- **Adjacency Matrix**: Natural representation for dense graphs
- **E ≈ V²**: Matrix-based Prim's is efficient O(V²)
- **Complete Graphs**: Every vertex connected to every other
- **Network Design**: Dense connectivity requirements

#### Vertex-Centric Problems
- **Growing from Source**: Natural to start from specific vertex
- **Incremental Construction**: Build MST by adding vertices one by one
- **Vertex Priorities**: When certain vertices should be processed first
- **Local Optimization**: Focus on immediate neighbors

#### Memory Efficiency (for Dense Graphs)
- **Adjacency Matrix Input**: Graph already in matrix form
- **Constant Space**: O(V) space regardless of edge count
- **Cache Locality**: Better memory access patterns for dense graphs
- **Simple Implementation**: Matrix version is straightforward

#### Real-Time Applications
- **Online Algorithms**: Can start immediately without sorting edges
- **Streaming Vertices**: Process vertices as they become available
- **Interactive Systems**: User can specify starting vertex
- **Incremental Updates**: Easy to modify when graph changes

### ❌ Avoid Prim's When:

#### Sparse Graphs
- **Use Kruskal's**: Better for E << V² scenarios
- **Edge List Input**: When edges are given as list
- **Union-Find Applications**: When disjoint set operations are needed

#### Very Large Graphs
- **Memory Constraints**: Matrix representation prohibitive
- **Distributed Processing**: Kruskal's edges can be processed in parallel

## Real-World Applications

### Network Infrastructure
- **Telecommunications**: Connect all network nodes with minimum cable
- **Power Grid**: Electrical distribution with minimum transmission lines
- **Water Distribution**: Pipeline networks for city water supply
- **Internet Backbone**: Core network topology optimization

### Transportation Systems
- **Railway Networks**: Connect all cities with minimum track length
- **Road Construction**: Highway systems with minimum total cost
- **Airline Hub Design**: Connect airports with minimum route costs
- **Public Transit**: Bus/metro networks with optimal coverage

### Circuit Design
- **PCB Layout**: Connect components with minimum trace length
- **VLSI Design**: Chip interconnections with minimal wire usage
- **Network Topology**: Computer network design for data centers
- **Sensor Networks**: Connect sensors with minimum energy consumption

### Facility Planning
- **Campus Design**: Connect buildings with minimum pathway cost
- **Industrial Layout**: Factory floor planning with material flow
- **Urban Planning**: City infrastructure with optimal connectivity
- **Supply Chain**: Distribution center connections

## Algorithm Variants

### Prim's with Custom Start Vertex
```python
def prim_from_vertex(graph, start_vertex):
    return prim(graph, start_vertex)
```

### Prim's for All Components
```python
def prim_forest(graph):
    visited_global = set()
    forest = []
    total_weight = 0
    
    for start in graph:
        if start not in visited_global:
            mst, weight = prim_component(graph, start, visited_global)
            forest.extend(mst)
            total_weight += weight
    
    return forest, total_weight
```

### Maximum Spanning Tree
```python
def prim_maximum_spanning_tree(graph, start=0):
    visited = set()
    mst = []
    total_weight = 0
    
    # Use negative weights for max-heap behavior
    pq = [(0, start, -1)]
    
    while pq:
        neg_weight, u, parent = heapq.heappop(pq)
        weight = -neg_weight
        
        if u in visited:
            continue
        
        visited.add(u)
        if parent != -1:
            mst.append((parent, u, weight))
            total_weight += weight
        
        for v, w in graph[u]:
            if v not in visited:
                heapq.heappush(pq, (-w, v, u))  # Negative for max-heap
    
    return mst, total_weight
```

## Comparison with Kruskal's Algorithm

| Aspect | Prim's | Kruskal's |
|--------|--------|-----------|
| **Time Complexity** | O(E log V) with heap | O(E log E) |
| **Space Complexity** | O(V) | O(V) |
| **Best For** | Dense graphs | Sparse graphs |
| **Data Structure** | Priority Queue | Union-Find |
| **Edge Processing** | Local (adjacent) | Global (all edges) |
| **Implementation** | Vertex-based | Edge-based |
| **Start Vertex** | Can specify | Any order |
| **Parallelization** | Limited | Better |

## Implementation Tips

### Graph Representation Choice
```python
# For dense graphs - adjacency matrix
matrix = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
          [4, 0, 8, 0, 0, 0, 0, 11, 0],
          # ... rest of matrix
         ]

# For sparse graphs - adjacency list
graph = {
    0: [(1, 4), (7, 8)],
    1: [(0, 4), (2, 8), (7, 11)],
    # ... rest of adjacency list
}
```

### Priority Queue Optimization
```python
# Use tuple ordering: (weight, vertex, parent)
# Python's heapq is min-heap by default
heapq.heappush(pq, (weight, vertex, parent))
```

### Handling Disconnected Graphs
```python
def prim_all_components(graph):
    visited_global = set()
    components = []
    
    for vertex in graph:
        if vertex not in visited_global:
            component_mst, weight = prim_component(graph, vertex, visited_global)
            components.append((component_mst, weight))
    
    return components
```

### Edge Cases
- **Single vertex**: MST is empty, weight is 0
- **No edges**: Each vertex is its own component
- **Disconnected graph**: Returns MST of reachable component only
- **Self-loops**: Ignored (don't contribute to spanning tree)

## Performance Considerations

### When Prim's Wins
- **Dense graphs**: E ≈ V², matrix version is O(V²)
- **Vertex-centric processing**: Natural starting point specified
- **Memory efficiency**: For dense graphs, uses less memory than edge list
- **Incremental construction**: Can stop early if partial MST needed

### When Kruskal's Wins
- **Sparse graphs**: E << V², sorting edges is efficient
- **Edge-centric processing**: Edges given as input list
- **Parallel processing**: Edge sorting and processing can be parallelized
- **Union-Find applications**: When disjoint set operations are useful

### Optimization Techniques
1. **Use appropriate data structure**: Heap for sparse, array for dense
2. **Early termination**: Stop when MST is complete (n-1 edges)
3. **Lazy deletion**: Don't remove outdated entries from priority queue
4. **Fibonacci heap**: For theoretical O(E + V log V) complexity

## Common Pitfalls

1. **Directed graphs**: Prim's only works for undirected graphs
2. **Disconnected graphs**: May not find complete MST
3. **Negative weights**: Algorithm works but may not be meaningful
4. **Duplicate edges**: Handle multiple edges between same vertices
5. **Starting vertex**: Ensure starting vertex exists in graph