# Floyd-Warshall Algorithm

The Floyd-Warshall algorithm finds shortest paths between all pairs of vertices in a weighted graph. It works with negative edge weights but detects negative cycles.

## Algorithm

### Basic Implementation
```python
def floyd_warshall(graph, n):
    # Initialize distance matrix
    dist = [[float('inf')] * n for _ in range(n)]
    
    # Distance from vertex to itself is 0
    for i in range(n):
        dist[i][i] = 0
    
    # Fill in direct edges
    for u in graph:
        for v, w in graph[u]:
            dist[u][v] = min(dist[u][v], w)
    
    # Main algorithm: try all intermediate vertices
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist
```

### With Path Reconstruction
```python
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
```

### Negative Cycle Detection
```python
def has_negative_cycle_floyd(dist, n):
    for i in range(n):
        if dist[i][i] < 0:
            return True
    return False
```

## Complexity Analysis

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| **Basic Algorithm** | **O(V³)** | **O(V²)** |
| **With Path Reconstruction** | **O(V³)** | **O(V²)** |
| **Path Reconstruction** | **O(V)** | **O(V)** |

## Where & When to Use?

### ✅ Use Floyd-Warshall When:

#### All-Pairs Shortest Paths Needed
- **Distance Matrices**: Need distances between every pair of vertices
- **Network Analysis**: Analyze connectivity between all nodes
- **Graph Metrics**: Compute diameter, radius, centrality measures
- **Routing Tables**: Precompute all possible routes

#### Dense Graphs
- **Complete or Near-Complete Graphs**: Most vertices connected
- **Small to Medium Graphs**: V ≤ 400-500 vertices typically
- **Matrix Operations**: When adjacency matrix is natural representation
- **Memory vs Time Trade-off**: Precompute for fast queries

#### Negative Edge Weights
- **Financial Networks**: Currency exchange with negative rates
- **Game Theory**: Payoff matrices with negative values
- **Cost Analysis**: Systems with penalties and rewards
- **Network Optimization**: Links with negative costs

#### Transitive Closure
- **Reachability Analysis**: Which vertices can reach which others
- **Dependency Analysis**: Transitive dependencies in systems
- **Social Networks**: Indirect connections and influence
- **Database Queries**: Recursive relationship queries

### ❌ Avoid Floyd-Warshall When:

#### Large Sparse Graphs
- **Use Johnson's Algorithm**: O(V² log V + VE) for sparse graphs
- **Use Multiple Dijkstra**: Run Dijkstra from each vertex
- **Memory Constraints**: O(V²) space becomes prohibitive

#### Single-Source Shortest Paths
- **Use Dijkstra**: Much faster for single source
- **Use Bellman-Ford**: If negative edges exist

#### Very Large Graphs
- **V > 1000**: Cubic time becomes impractical
- **Streaming Data**: Cannot fit entire matrix in memory

## Real-World Applications

### Network Analysis
- **Internet Routing**: Precompute routing tables for fast lookup
- **Social Networks**: Find shortest paths between any two users
- **Transportation**: Distance matrices for logistics planning
- **Communication Networks**: Optimize message routing

### Game Development
- **Pathfinding**: Precompute distances in small game worlds
- **AI Planning**: Strategic decision making with complete information
- **Map Analysis**: Analyze connectivity and strategic positions
- **Resource Management**: Optimize resource distribution

### Operations Research
- **Supply Chain**: Optimize distribution networks
- **Facility Location**: Analyze accessibility from all locations
- **Scheduling**: Minimize total travel time in systems
- **Logistics**: Route planning with multiple origins/destinations

### Graph Theory Applications
- **Graph Diameter**: Find longest shortest path
- **Graph Center**: Find most central vertices
- **Clustering**: Analyze graph structure and communities
- **Connectivity**: Analyze robustness and critical paths

## Algorithm Variants

### Transitive Closure (Warshall's Algorithm)
```python
def transitive_closure(graph, n):
    reach = [[False] * n for _ in range(n)]
    
    # Initialize direct reachability
    for i in range(n):
        reach[i][i] = True
    
    for u in graph:
        for v in graph[u]:
            reach[u][v] = True
    
    # Compute transitive closure
    for k in range(n):
        for i in range(n):
            for j in range(n):
                reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])
    
    return reach
```

### Minimax Path (Bottleneck Shortest Path)
```python
def floyd_minimax(graph, n):
    dist = [[float('inf')] * n for _ in range(n)]
    
    for i in range(n):
        dist[i][i] = 0
    
    for u in graph:
        for v, w in graph[u]:
            dist[u][v] = w
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], max(dist[i][k], dist[k][j]))
    
    return dist
```

### Maximum Reliability Path
```python
def floyd_max_reliability(graph, n):
    # Reliability values between 0 and 1
    reliability = [[0.0] * n for _ in range(n)]
    
    for i in range(n):
        reliability[i][i] = 1.0
    
    for u in graph:
        for v, r in graph[u]:
            reliability[u][v] = r
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                reliability[i][j] = max(reliability[i][j], 
                                     reliability[i][k] * reliability[k][j])
    
    return reliability
```

## Optimization Techniques

### Space Optimization
```python
def floyd_warshall_space_optimized(adj_matrix):
    n = len(adj_matrix)
    # Modify matrix in-place
    dist = adj_matrix
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist
```

### Early Termination
```python
def floyd_warshall_early_termination(graph, n):
    dist = [[float('inf')] * n for _ in range(n)]
    
    # Initialize
    for i in range(n):
        dist[i][i] = 0
    for u in graph:
        for v, w in graph[u]:
            dist[u][v] = min(dist[u][v], w)
    
    for k in range(n):
        changed = False
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    changed = True
        
        if not changed:
            break  # No more improvements possible
    
    return dist
```

## Comparison with Other Algorithms

| Use Case | Floyd-Warshall | Johnson's | Multiple Dijkstra |
|----------|----------------|-----------|-------------------|
| **Dense Graph** | ✅ O(V³) | ❌ O(V² log V + VE) | ❌ O(V(V+E) log V) |
| **Sparse Graph** | ❌ O(V³) | ✅ O(V² log V + VE) | ✅ O(V(V+E) log V) |
| **Negative Edges** | ✅ | ✅ | ❌ |
| **Memory Usage** | ❌ O(V²) | ✅ O(V) | ✅ O(V) |
| **Implementation** | ✅ Simple | ❌ Complex | ✅ Simple |

## Implementation Tips

### Input Handling
```python
# Handle multiple edges between same vertices
for u in graph:
    for v, w in graph[u]:
        dist[u][v] = min(dist[u][v], w)  # Take minimum weight
```

### Infinity Handling
```python
# Avoid overflow in addition
if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
```

### Common Applications
1. **Shortest Path Queries**: Answer queries in O(1) after preprocessing
2. **Graph Diameter**: max(dist[i][j]) for all i,j
3. **Graph Radius**: min(max(dist[i][j] for j)) for all i
4. **Eccentricity**: max(dist[i][j]) for fixed i, all j