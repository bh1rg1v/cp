# Johnson's Algorithm

Johnson's algorithm finds shortest paths between all pairs of vertices in a sparse, weighted graph. It handles negative edge weights but not negative cycles.

## Algorithm Overview

Johnson's algorithm combines Bellman-Ford and Dijkstra's algorithms:
1. **Add auxiliary vertex** connected to all vertices with weight 0
2. **Run Bellman-Ford** from auxiliary vertex to detect negative cycles and compute potential function
3. **Reweight edges** using potential function to make all weights non-negative
4. **Run Dijkstra** from each vertex on reweighted graph
5. **Convert distances** back to original weights

## Implementation

### Basic Johnson's Algorithm
```python
def johnson_all_pairs(graph, n):
    # Step 1: Add auxiliary vertex
    extended_graph = defaultdict(list)
    for u in graph:
        for v, w in graph[u]:
            extended_graph[u].append((v, w))
    
    for i in range(n):
        extended_graph[n].append((i, 0))  # Auxiliary vertex n
    
    # Step 2: Run Bellman-Ford from auxiliary vertex
    h = bellman_ford_johnson(extended_graph, n, n + 1)
    if h is None:
        return None  # Negative cycle detected
    
    # Step 3: Reweight edges
    reweighted_graph = defaultdict(list)
    for u in graph:
        for v, w in graph[u]:
            new_weight = w + h[u] - h[v]  # Johnson's reweighting
            reweighted_graph[u].append((v, new_weight))
    
    # Step 4: Run Dijkstra from each vertex
    all_distances = {}
    for u in range(n):
        dist = dijkstra_johnson(reweighted_graph, u, h)
        
        # Step 5: Convert back to original distances
        original_dist = {}
        for v in dist:
            if dist[v] != float('inf'):
                original_dist[v] = dist[v] - h[u] + h[v]
            else:
                original_dist[v] = float('inf')
        
        all_distances[u] = original_dist
    
    return all_distances
```

### Reweighting Function
The key insight is Johnson's reweighting formula:
```
w'(u,v) = w(u,v) + h(u) - h(v)
```
Where `h` is the potential function from Bellman-Ford.

### Dijkstra with Reweighted Edges
```python
def dijkstra_johnson(graph, start, h):
    dist = defaultdict(lambda: float('inf'))
    dist[start] = 0
    pq = [(0, start)]
    
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
            
        for v, w in graph[u]:
            new_weight = w + h[u] - h[v]  # Already reweighted
            if dist[u] + new_weight < dist[v]:
                dist[v] = dist[u] + new_weight
                heapq.heappush(pq, (dist[v], v))
    
    return dict(dist)
```

## Complexity Analysis

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| **Bellman-Ford** | **O(VE)** | **O(V)** |
| **V × Dijkstra** | **O(V² log V + VE)** | **O(V)** |
| **Total** | **O(V² log V + VE)** | **O(V²)** |

## Where & When to Use?

### ✅ Use Johnson's Algorithm When:

#### Sparse Graphs with Negative Edges
- **Network Routing**: Routes with penalties or negative costs
- **Financial Networks**: Currency exchange with negative rates
- **Game Theory**: Payoff matrices with negative values
- **Transportation**: Routes with tolls, discounts, or penalties

#### All-Pairs Shortest Paths on Sparse Graphs
- **E << V²**: Much more efficient than Floyd-Warshall
- **Multiple Queries**: Need distances between all vertex pairs
- **Preprocessing**: Precompute for fast distance queries
- **Graph Analysis**: Compute diameter, radius, centrality measures

#### Better than Alternatives
- **vs Floyd-Warshall**: Better for sparse graphs (E << V²)
- **vs V × Bellman-Ford**: Much faster O(V² log V + VE) vs O(V²E)
- **vs V × Dijkstra**: Handles negative edges unlike pure Dijkstra

#### Memory Efficiency
- **Large Sparse Graphs**: More memory efficient than Floyd-Warshall
- **Streaming Applications**: Can process one source at a time
- **Distributed Computing**: Dijkstra calls can be parallelized

### ❌ Avoid Johnson's When:

#### Dense Graphs
- **Use Floyd-Warshall**: O(V³) vs O(V² log V + VE) when E ≈ V²
- **Simple Implementation**: Floyd-Warshall is easier to implement
- **Matrix Operations**: When adjacency matrix is natural

#### No Negative Edges
- **Use V × Dijkstra**: Simpler and slightly faster
- **No Reweighting Needed**: Avoid unnecessary complexity

#### Very Small Graphs
- **V ≤ 100**: Floyd-Warshall might be simpler and sufficient
- **Constant Factors**: Johnson's has higher constant factors

## Real-World Applications

### Transportation Networks
- **Multi-Modal Transport**: Different transport modes with transfers
- **Route Planning**: GPS systems with traffic penalties/bonuses
- **Logistics**: Delivery networks with time windows and penalties
- **Public Transit**: Bus/train networks with transfer costs

### Financial Systems
- **Currency Arbitrage**: Multi-currency exchange rate analysis
- **Portfolio Optimization**: Asset correlation with transaction costs
- **Risk Analysis**: Credit networks with positive/negative relationships
- **Trading Networks**: Market maker networks with spreads

### Network Analysis
- **Social Networks**: Influence propagation with positive/negative effects
- **Communication Networks**: Message routing with QoS requirements
- **Internet Routing**: BGP with policy-based routing costs
- **Sensor Networks**: Data aggregation with energy costs

### Game Theory and AI
- **Strategic Games**: Multi-player games with alliances/conflicts
- **Pathfinding**: Game worlds with buffs/debuffs affecting movement
- **Decision Trees**: Multi-criteria optimization problems
- **Resource Management**: Systems with synergies and conflicts

## Algorithm Variants

### Johnson's with Path Reconstruction
```python
def johnson_with_path(graph, n):
    # ... (reweighting steps same as above) ...
    
    all_distances = {}
    all_parents = {}
    
    for u in range(n):
        dist, parent = dijkstra_with_path(reweighted_graph, u)
        
        # Convert distances back
        original_dist = {}
        for v in dist:
            if dist[v] != float('inf'):
                original_dist[v] = dist[v] - h[u] + h[v]
            else:
                original_dist[v] = float('inf')
        
        all_distances[u] = original_dist
        all_parents[u] = parent
    
    return all_distances, all_parents
```

### Optimized for Edge List
```python
def johnson_sparse_optimized(edges, n):
    # Work directly with edge list for better cache performance
    extended_edges = edges + [(n, i, 0) for i in range(n)]
    
    # Bellman-Ford on edge list
    dist = [float('inf')] * (n + 1)
    dist[n] = 0
    
    for _ in range(n):
        for u, v, w in extended_edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    
    # Check for negative cycles
    for u, v, w in extended_edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            return None
    
    h = dist[:n]
    
    # Build reweighted adjacency list and run Dijkstra
    # ... (rest of implementation)
```

### Parallel Johnson's
```python
def johnson_parallel(graph, n):
    # Reweighting phase (sequential)
    h = compute_potential_function(graph, n)
    if h is None:
        return None
    
    reweighted_graph = reweight_edges(graph, h)
    
    # Parallel Dijkstra phase
    from concurrent.futures import ThreadPoolExecutor
    
    def dijkstra_for_source(u):
        return u, dijkstra_johnson(reweighted_graph, u, h)
    
    all_distances = {}
    with ThreadPoolExecutor() as executor:
        results = executor.map(dijkstra_for_source, range(n))
        for u, dist in results:
            # Convert back to original distances
            original_dist = {v: d - h[u] + h[v] for v, d in dist.items()}
            all_distances[u] = original_dist
    
    return all_distances
```

## Comparison with Other Algorithms

| Algorithm | Time | Space | Negative Edges | Best For |
|-----------|------|-------|----------------|----------|
| **Johnson's** | O(V² log V + VE) | O(V²) | ✅ | Sparse graphs |
| **Floyd-Warshall** | O(V³) | O(V²) | ✅ | Dense graphs |
| **V × Dijkstra** | O(V(V+E) log V) | O(V²) | ❌ | No negative edges |
| **V × Bellman-Ford** | O(V²E) | O(V²) | ✅ | Simple implementation |

## Implementation Tips

### Potential Function Properties
The potential function h must satisfy:
- **h(v) ≤ h(u) + w(u,v)** for all edges (u,v)
- This ensures **w'(u,v) = w(u,v) + h(u) - h(v) ≥ 0**

### Auxiliary Vertex Technique
```python
# Add auxiliary vertex connected to all vertices with weight 0
for i in range(n):
    extended_graph[n].append((i, 0))
```
This ensures all vertices are reachable from auxiliary vertex.

### Distance Conversion
```python
# Original distance = reweighted distance - h(source) + h(target)
original_distance = reweighted_distance - h[u] + h[v]
```

### Memory Optimization
```python
# Process one source at a time to save memory
def johnson_memory_efficient(graph, n):
    h = compute_potential_function(graph, n)
    
    for u in range(n):
        yield u, dijkstra_johnson_single(graph, u, h)
```

## Common Pitfalls

1. **Negative Cycles**: Always check Bellman-Ford result
2. **Auxiliary Vertex**: Don't forget to add connections to all vertices
3. **Distance Conversion**: Remember to convert back from reweighted distances
4. **Graph Representation**: Ensure consistent edge format throughout
5. **Infinity Handling**: Handle unreachable vertices properly

## Performance Considerations

### When Johnson's Wins
- **Sparse graphs**: E = O(V) or E = O(V log V)
- **Large graphs**: V > 1000 with E << V²
- **Multiple queries**: Need all-pairs distances repeatedly

### When to Use Alternatives
- **Dense graphs**: E ≈ V², use Floyd-Warshall
- **Single source**: Use Dijkstra or Bellman-Ford
- **No negative edges**: Use simpler V × Dijkstra