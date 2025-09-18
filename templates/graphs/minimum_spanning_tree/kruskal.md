# Kruskal's Algorithm

Kruskal's algorithm finds a minimum spanning tree (MST) of a connected, undirected graph using a greedy approach with Union-Find data structure.

## Algorithm

### Basic Implementation
```python
def kruskal(edges, n):
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])
    uf = UnionFind(n)
    mst = []
    total_weight = 0
    
    for u, v, w in edges:
        if uf.union(u, v):  # If u and v are in different components
            mst.append((u, v, w))
            total_weight += w
            
            if len(mst) == n - 1:  # MST complete
                break
    
    return mst, total_weight
```

### Union-Find Data Structure
```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False  # Already in same component
        
        # Union by rank
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        
        self.components -= 1
        return True
```

### With Connectivity Validation
```python
def kruskal_with_validation(edges, n):
    edges.sort(key=lambda x: x[2])
    uf = UnionFind(n)
    mst = []
    total_weight = 0
    
    for u, v, w in edges:
        if uf.union(u, v):
            mst.append((u, v, w))
            total_weight += w
    
    # Check if graph is connected
    if len(mst) != n - 1:
        return None, None  # Graph is not connected
    
    return mst, total_weight
```

## Complexity Analysis

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| **Sorting Edges** | **O(E log E)** | **O(1)** |
| **Union-Find Operations** | **O(E α(V))** | **O(V)** |
| **Total** | **O(E log E)** | **O(V)** |

*α(V) is the inverse Ackermann function, practically constant*

## Where & When to Use?

### ✅ Use Kruskal's Algorithm When:

#### Sparse Graphs
- **Few Edges**: E << V², edge-based approach is efficient
- **Network Design**: Connecting cities with minimum cable cost
- **Circuit Design**: Minimum wire length for connectivity
- **Transportation**: Minimum road construction cost

#### Edge-Centric Problems
- **Edge List Representation**: Natural when edges are given as list
- **Edge Processing**: Need to process edges in weight order
- **Incremental Construction**: Build MST by adding edges one by one
- **Edge Filtering**: Remove expensive edges while maintaining connectivity

#### Union-Find Applications
- **Dynamic Connectivity**: Track connected components during construction
- **Cycle Detection**: Union-Find naturally detects cycles
- **Component Analysis**: Need to know when components merge
- **Disjoint Set Operations**: Part of larger Union-Find based solution

#### Distributed/Parallel Processing
- **Edge Sorting**: Can be parallelized efficiently
- **Independent Edge Processing**: Edges can be processed independently
- **Distributed Systems**: Suitable for distributed MST algorithms
- **Large Datasets**: Works well with external sorting

### ❌ Avoid Kruskal's When:

#### Dense Graphs
- **Use Prim's Algorithm**: Better for dense graphs (E ≈ V²)
- **Adjacency Matrix**: When graph is represented as matrix
- **Vertex-Centric**: When processing vertices is more natural

#### Memory Constraints
- **Large Edge Lists**: Storing all edges may be prohibitive
- **Streaming Edges**: Cannot sort all edges in advance
- **Limited Memory**: Prim's uses less memory for dense graphs

## Real-World Applications

### Network Infrastructure
- **Telecommunications**: Minimum cost to connect all network nodes
- **Internet Backbone**: Design efficient routing infrastructure
- **Power Grid**: Connect all substations with minimum transmission lines
- **Water Distribution**: Minimum pipeline network for city coverage

### Transportation Systems
- **Road Networks**: Connect all cities with minimum road construction
- **Railway Planning**: Optimal rail network design
- **Airline Routes**: Hub-and-spoke network optimization
- **Supply Chain**: Minimum cost distribution network

### Computer Networks
- **LAN Design**: Connect all computers with minimum cable
- **Wireless Networks**: Optimize wireless access point placement
- **Sensor Networks**: Connect sensors with minimum energy consumption
- **Data Centers**: Optimize internal network topology

### Manufacturing
- **Circuit Board Design**: Minimum trace length for connectivity
- **Pipeline Networks**: Oil, gas, or chemical distribution
- **Facility Layout**: Connect production units efficiently
- **Logistics**: Warehouse and distribution center connections

## Algorithm Variants

### Maximum Spanning Tree
```python
def kruskal_maximum_spanning_tree(edges, n):
    # Sort edges in descending order of weight
    edges.sort(key=lambda x: x[2], reverse=True)
    uf = UnionFind(n)
    mst = []
    total_weight = 0
    
    for u, v, w in edges:
        if uf.union(u, v):
            mst.append((u, v, w))
            total_weight += w
            if len(mst) == n - 1:
                break
    
    return mst, total_weight
```

### K-Minimum Spanning Tree
```python
def k_minimum_spanning_trees(edges, n, k):
    edges.sort(key=lambda x: x[2])
    results = []
    
    # Generate k different MSTs using different tie-breaking rules
    for iteration in range(k):
        uf = UnionFind(n)
        mst = []
        total_weight = 0
        
        for i, (u, v, w) in enumerate(edges):
            if uf.union(u, v):
                mst.append((u, v, w))
                total_weight += w
                if len(mst) == n - 1:
                    break
        
        if len(mst) == n - 1:
            results.append((mst, total_weight))
        
        # Modify edge order for next iteration
        # (Implementation depends on specific requirements)
    
    return results
```

### Minimum Bottleneck Spanning Tree
```python
def minimum_bottleneck_spanning_tree(edges, n):
    edges.sort(key=lambda x: x[2])
    uf = UnionFind(n)
    max_edge_weight = 0
    
    for u, v, w in edges:
        if uf.union(u, v):
            max_edge_weight = max(max_edge_weight, w)
            if uf.components == 1:
                break
    
    return max_edge_weight
```

## Comparison with Prim's Algorithm

| Aspect | Kruskal's | Prim's |
|--------|-----------|--------|
| **Time Complexity** | O(E log E) | O(E log V) with heap |
| **Space Complexity** | O(V) | O(V) |
| **Best For** | Sparse graphs | Dense graphs |
| **Data Structure** | Union-Find | Priority Queue |
| **Edge Processing** | Global (all edges) | Local (adjacent edges) |
| **Implementation** | Edge-based | Vertex-based |

## Optimization Techniques

### Early Termination
```python
def kruskal_early_termination(edges, n):
    edges.sort(key=lambda x: x[2])
    uf = UnionFind(n)
    mst = []
    total_weight = 0
    
    for u, v, w in edges:
        if uf.union(u, v):
            mst.append((u, v, w))
            total_weight += w
            
            # Early termination when MST is complete
            if len(mst) == n - 1:
                break
    
    return mst, total_weight
```

### Filtering Edges
```python
def kruskal_with_filtering(edges, n, max_weight=None):
    # Filter edges by weight threshold
    if max_weight is not None:
        edges = [(u, v, w) for u, v, w in edges if w <= max_weight]
    
    edges.sort(key=lambda x: x[2])
    uf = UnionFind(n)
    mst = []
    total_weight = 0
    
    for u, v, w in edges:
        if uf.union(u, v):
            mst.append((u, v, w))
            total_weight += w
    
    return mst, total_weight
```

## Implementation Tips

### Edge Input Formats
```python
# From adjacency list
def edges_from_adjacency_list(graph):
    edges = []
    for u in graph:
        for v, w in graph[u]:
            if u < v:  # Avoid duplicate edges in undirected graph
                edges.append((u, v, w))
    return edges

# From adjacency matrix
def edges_from_adjacency_matrix(matrix):
    n = len(matrix)
    edges = []
    for i in range(n):
        for j in range(i + 1, n):  # Upper triangle only
            if matrix[i][j] != float('inf') and matrix[i][j] != 0:
                edges.append((i, j, matrix[i][j]))
    return edges
```

### Handling Disconnected Graphs
```python
def kruskal_forest(edges, n):
    """Returns minimum spanning forest for disconnected graph"""
    edges.sort(key=lambda x: x[2])
    uf = UnionFind(n)
    forest = []
    total_weight = 0
    
    for u, v, w in edges:
        if uf.union(u, v):
            forest.append((u, v, w))
            total_weight += w
    
    return forest, total_weight, uf.components
```

### Common Pitfalls
1. **Directed Graphs**: Kruskal's only works for undirected graphs
2. **Duplicate Edges**: Handle multiple edges between same vertices
3. **Self-Loops**: Remove self-loops before processing
4. **Disconnected Graphs**: Check if MST is possible (n-1 edges)