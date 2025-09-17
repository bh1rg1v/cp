# Adjacency Matrix Representation

An adjacency matrix represents a graph as a 2D array where `matrix[i][j]` indicates the presence (and weight) of an edge from vertex i to vertex j.

## Structure

```python
# For V vertices
matrix = [[0] * V for _ in range(V)]

# matrix[i][j] = weight if edge exists, 0 otherwise
matrix[u][v] = weight  # Edge from u to v
```

## Implementation

```python
class AdjacencyMatrix:
    def __init__(self, num_vertices, directed=False):
        self.num_vertices = num_vertices
        self.directed = directed
        self.matrix = [[0] * num_vertices for _ in range(num_vertices)]
    
    def add_edge(self, u, v, weight=1):
        self.matrix[u][v] = weight
        if not self.directed:
            self.matrix[v][u] = weight
```

## Operations Complexity

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| **Add Edge** | **O(1)** | O(1) |
| **Remove Edge** | **O(1)** | O(1) |
| **Check Edge** | **O(1)** | O(1) |
| **Get Neighbors** | **O(V)** | O(V) |
| **Space Total** | **O(V²)** | - |

## Memory Usage

- **Space**: O(V²) regardless of actual edge count
- **Fixed size**: Must pre-allocate for maximum vertices
- **Uniform access**: Every cell takes same memory

## Advantages

### Constant Time Operations
- **Edge queries**: O(1) to check if edge exists
- **Edge weights**: O(1) to get/set edge weight
- **Edge updates**: O(1) to add/remove edges

### Simple Implementation
- **2D array**: Straightforward data structure
- **No pointers**: Direct array indexing
- **Cache friendly**: Contiguous memory layout

### Matrix Operations
- **Graph algorithms**: Easy to implement matrix-based algorithms
- **Mathematical operations**: Matrix multiplication for path counting
- **Symmetric properties**: Easy to enforce undirected graph constraints

## Disadvantages

### Memory Inefficient
- **Sparse graphs**: Wastes O(V²) space even with few edges
- **Large graphs**: Prohibitive memory for millions of vertices
- **Fixed size**: Cannot dynamically grow

### Slow Neighbor Iteration
- **Find neighbors**: Must scan entire row O(V)
- **Graph traversal**: Inefficient for DFS/BFS
- **Degree calculation**: O(V) to count non-zero entries

## When to Use Adjacency Matrix

### ✅ Ideal For:

#### Dense Graphs
- **Complete graphs**: Most vertices connected to most others
- **Near-complete graphs**: High edge-to-vertex ratio
- **Cliques**: Subgraphs where every vertex connects to every other

#### Frequent Edge Queries
- **Pathfinding**: Need fast "is there an edge?" checks
- **Graph analysis**: Algorithms that query many edge weights
- **Interactive applications**: User frequently checks connections

#### Mathematical Graph Operations
- **Matrix multiplication**: Computing paths of specific lengths
- **Graph powers**: A^k gives paths of length k
- **Spectral analysis**: Eigenvalues and eigenvectors of adjacency matrix

#### Small Graphs
- **V ≤ 1000**: Memory usage acceptable
- **Fixed size**: Number of vertices known and small
- **Performance critical**: Need fastest possible edge access

### ❌ Avoid When:

#### Sparse Graphs
- **Social networks**: Average person has << 1000 friends
- **Web graphs**: Pages link to tiny fraction of all pages
- **Transportation**: Cities connect to few neighboring cities

#### Large Graphs
- **V > 10,000**: Memory becomes prohibitive
- **Streaming data**: Graph size grows dynamically
- **Memory constraints**: Limited RAM available

#### Traversal-Heavy Algorithms
- **DFS/BFS**: Spend most time iterating neighbors
- **Shortest path**: Dijkstra's algorithm iterates neighbors frequently
- **Graph coloring**: Need efficient neighbor access

## Example Use Cases

### Game Board Analysis
```python
# Chess board - piece attack patterns
board = AdjacencyMatrix(64)  # 8x8 = 64 squares

# Queen at position 27 can attack position 35
board.add_edge(27, 35, 1)

# Fast lookup: can piece at pos1 attack pos2?
def can_attack(pos1, pos2):
    return board.has_edge(pos1, pos2)  # O(1)
```

### Network Topology
```python
# Small network with known routers
network = AdjacencyMatrix(10, directed=True)
network.add_edge(0, 1, 100)  # Router 0 -> Router 1, bandwidth 100

# Fast connectivity matrix for routing decisions
def direct_connection_bandwidth(router1, router2):
    return network.get_weight(router1, router2)  # O(1)
```

### Mathematical Graph Analysis
```python
# Compute number of paths of length k
def paths_of_length_k(matrix, k):
    result = matrix.copy()
    for _ in range(k-1):
        result = matrix_multiply(result, matrix)
    return result

# Adjacency matrix makes this computation natural
```

## Implementation Variants

### Boolean Matrix (Unweighted)
```python
matrix = [[False] * V for _ in range(V)]
matrix[u][v] = True  # Edge exists
```

### Weight Matrix (Weighted)
```python
matrix = [[float('inf')] * V for _ in range(V)]
for i in range(V):
    matrix[i][i] = 0  # Distance to self is 0
matrix[u][v] = weight  # Edge weight
```

### Compressed Sparse Row (CSR)
```python
# For sparse matrices - hybrid approach
class CSRMatrix:
    def __init__(self):
        self.data = []      # Non-zero values
        self.indices = []   # Column indices
        self.indptr = []    # Row pointers
```

## Performance Comparison

### vs Adjacency List

| Aspect | Adjacency Matrix | Adjacency List |
|--------|------------------|----------------|
| **Space** | O(V²) | O(V + E) |
| **Add Edge** | O(1) | O(1) |
| **Check Edge** | O(1) | O(degree) |
| **Iterate Neighbors** | O(V) | O(degree) |
| **Best For** | Dense graphs | Sparse graphs |

### Memory Usage Examples

#### Small Dense Graph (V=100, E=5000)
- **Adjacency Matrix**: 40KB (100² × 4 bytes)
- **Adjacency List**: 40KB (similar for dense)
- **Matrix advantage**: Faster edge queries

#### Large Sparse Graph (V=100000, E=200000)  
- **Adjacency Matrix**: 40GB (100000² × 4 bytes)
- **Adjacency List**: 1.6MB (200000 × 8 bytes)
- **List advantage**: 25,000x less memory

## Matrix-Based Algorithms

### Transitive Closure (Floyd-Warshall)
```python
def floyd_warshall(matrix):
    V = len(matrix)
    dist = [row[:] for row in matrix]  # Copy matrix
    
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], 
                               dist[i][k] + dist[k][j])
    return dist
```

### Matrix Powers for Path Counting
```python
def count_paths_length_k(adj_matrix, k):
    """Count paths of exactly length k between all pairs"""
    result = identity_matrix(len(adj_matrix))
    base = adj_matrix
    
    while k > 0:
        if k & 1:
            result = matrix_multiply(result, base)
        base = matrix_multiply(base, base)
        k >>= 1
    
    return result
```

### Graph Connectivity
```python
def is_connected(matrix):
    """Check if undirected graph is connected"""
    V = len(matrix)
    
    # DFS from vertex 0
    visited = [False] * V
    stack = [0]
    visited[0] = True
    count = 1
    
    while stack:
        u = stack.pop()
        for v in range(V):
            if matrix[u][v] and not visited[v]:
                visited[v] = True
                stack.append(v)
                count += 1
    
    return count == V
```

## Best Practices

### Memory Management
```python
# For large matrices, consider sparse representations
import numpy as np
from scipy.sparse import csr_matrix

# Use numpy for better memory efficiency
matrix = np.zeros((V, V), dtype=np.int32)

# Or sparse matrix for very sparse graphs
sparse_matrix = csr_matrix((V, V))
```

### Initialization Patterns
```python
# Unweighted graph
matrix = [[0] * V for _ in range(V)]

# Weighted graph (use infinity for no edge)
matrix = [[float('inf')] * V for _ in range(V)]
for i in range(V):
    matrix[i][i] = 0  # Self-loops have weight 0

# Boolean adjacency
matrix = [[False] * V for _ in range(V)]
```

### Performance Optimization
```python
# Cache-friendly neighbor iteration
def get_neighbors_fast(matrix, vertex):
    return [i for i, weight in enumerate(matrix[vertex]) if weight != 0]

# Batch edge operations
def add_edges_batch(matrix, edges):
    for u, v, weight in edges:
        matrix[u][v] = weight
        matrix[v][u] = weight  # If undirected
```

## Decision Framework

**Choose Adjacency Matrix when:**
- Graph is dense (E ≈ V²)
- Frequent edge existence queries
- Small number of vertices (V < 1000)
- Need matrix mathematical operations
- Memory is not a constraint

**Choose Adjacency List when:**
- Graph is sparse (E << V²)
- Frequent neighbor iteration
- Large number of vertices
- Memory efficiency important
- Dynamic graph structure