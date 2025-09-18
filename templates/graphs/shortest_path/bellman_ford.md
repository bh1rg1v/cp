# Bellman-Ford Algorithm

The Bellman-Ford algorithm finds shortest paths from a single source vertex to all other vertices in a weighted graph, and can detect negative weight cycles.

## Algorithm

### Basic Implementation
```python
def bellman_ford(graph, start, n):
    dist = [float('inf')] * n
    dist[start] = 0
    
    # Relax edges n-1 times
    for _ in range(n - 1):
        for u in graph:
            if dist[u] != float('inf'):
                for v, w in graph[u]:
                    if dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
    
    # Check for negative cycles
    for u in graph:
        if dist[u] != float('inf'):
            for v, w in graph[u]:
                if dist[u] + w < dist[v]:
                    return None  # Negative cycle detected
    
    return dist
```

### With Path Reconstruction
```python
def bellman_ford_with_path(graph, start, n):
    dist = [float('inf')] * n
    parent = [-1] * n
    dist[start] = 0
    
    for _ in range(n - 1):
        for u in graph:
            if dist[u] != float('inf'):
                for v, w in graph[u]:
                    if dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
                        parent[v] = u
    
    # Negative cycle check
    for u in graph:
        if dist[u] != float('inf'):
            for v, w in graph[u]:
                if dist[u] + w < dist[v]:
                    return None, None
    
    return dist, parent
```

### Negative Cycle Detection
```python
def detect_negative_cycle(graph, n):
    dist = [0] * n  # Start with all zeros
    
    for _ in range(n - 1):
        for u in graph:
            for v, w in graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
    
    # Check if any distance can still be improved
    for u in graph:
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                return True
    
    return False
```

## Complexity Analysis

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| **Basic Algorithm** | **O(VE)** | **O(V)** |
| **With Path Reconstruction** | **O(VE)** | **O(V)** |
| **Negative Cycle Detection** | **O(VE)** | **O(V)** |

## Where & When to Use?

### ✅ Use Bellman-Ford When:

#### Negative Edge Weights
- **Currency Exchange**: Detect arbitrage opportunities (negative cycles)
- **Game Theory**: Paths with penalties or costs that can be negative
- **Network Routing**: Links with negative costs or penalties
- **Financial Modeling**: Profit/loss calculations with negative values

#### Negative Cycle Detection Required
- **Arbitrage Detection**: Currency trading, commodity markets
- **Game Balance**: Detect infinite loops in game mechanics
- **Economic Models**: Identify unsustainable economic cycles
- **Network Analysis**: Find problematic routing loops

#### Distributed Systems
- **Distance Vector Routing**: Bellman-Ford is basis for RIP protocol
- **Distributed Shortest Path**: Each node runs local computation
- **Network Protocols**: BGP uses path vector (Bellman-Ford variant)
- **Fault Tolerance**: Handles link failures and recovers

#### Simple Implementation Needed
- **Educational Purposes**: Easier to understand than Dijkstra
- **Proof of Correctness**: Mathematical analysis is straightforward
- **Small Graphs**: When performance is not critical
- **Debugging**: Easier to trace and verify results

### ❌ Avoid Bellman-Ford When:

#### Non-negative Weights Only
- **Use Dijkstra instead**: O((V + E) log V) vs O(VE)
- **Performance Critical**: Bellman-Ford is much slower
- **Large Graphs**: Quadratic behavior becomes prohibitive

#### All-Pairs Shortest Paths
- **Use Floyd-Warshall**: Better for dense graphs
- **Use Johnson's Algorithm**: Better for sparse graphs with negative edges

## Real-World Applications

### Financial Systems
- **Currency Exchange**: Find best exchange rates, detect arbitrage
- **Portfolio Optimization**: Handle short selling (negative positions)
- **Risk Analysis**: Model scenarios with losses and gains
- **Trading Algorithms**: Detect profitable cycles in markets

### Network Protocols
- **RIP (Routing Information Protocol)**: Uses distance vector algorithm
- **BGP Path Selection**: Modified Bellman-Ford for policy routing
- **Network Troubleshooting**: Detect routing loops and black holes
- **Quality of Service**: Route selection with negative penalties

### Game Development
- **Pathfinding with Penalties**: Avoid dangerous areas (negative weights)
- **Resource Management**: Costs and benefits in strategy games
- **AI Decision Making**: Evaluate actions with positive/negative outcomes
- **Balance Testing**: Detect overpowered combinations (negative cycles)

### Operations Research
- **Supply Chain**: Model costs, penalties, and incentives
- **Project Management**: Handle penalties for delays
- **Resource Allocation**: Optimize with constraints and penalties
- **Scheduling**: Account for setup costs and change penalties

## Algorithm Variants

### SPFA (Shortest Path Faster Algorithm)
```python
def spfa(graph, start, n):
    dist = [float('inf')] * n
    in_queue = [False] * n
    count = [0] * n
    
    queue = deque([start])
    dist[start] = 0
    in_queue[start] = True
    
    while queue:
        u = queue.popleft()
        in_queue[u] = False
        
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                count[v] += 1
                
                if count[v] >= n:
                    return None  # Negative cycle
                
                if not in_queue[v]:
                    queue.append(v)
                    in_queue[v] = True
    
    return dist
```

### Early Termination Optimization
```python
def bellman_ford_optimized(graph, start, n):
    dist = [float('inf')] * n
    dist[start] = 0
    
    for i in range(n - 1):
        updated = False
        
        for u in graph:
            if dist[u] != float('inf'):
                for v, w in graph[u]:
                    if dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
                        updated = True
        
        if not updated:
            break  # No more updates possible
    
    return dist
```

## Comparison with Other Algorithms

| Algorithm | Time | Space | Negative Edges | Negative Cycles |
|-----------|------|-------|----------------|-----------------|
| **Bellman-Ford** | O(VE) | O(V) | ✅ | ✅ Detects |
| **Dijkstra** | O((V+E) log V) | O(V) | ❌ | ❌ |
| **Floyd-Warshall** | O(V³) | O(V²) | ✅ | ✅ Detects |
| **SPFA** | O(VE) avg, O(VE) worst | O(V) | ✅ | ✅ Detects |

## Implementation Tips

### Edge Representation
```python
# Adjacency list (preferred for sparse graphs)
graph = defaultdict(list)
graph[u].append((v, weight))

# Edge list (simpler for some implementations)
edges = [(u, v, weight), ...]
```

### Negative Cycle Handling
```python
def find_negative_cycle_nodes(graph, n):
    dist = [0] * n
    
    # Run Bellman-Ford
    for _ in range(n - 1):
        for u in graph:
            for v, w in graph[u]:
                dist[v] = min(dist[v], dist[u] + w)
    
    # Find nodes affected by negative cycles
    affected = set()
    for _ in range(n):
        for u in graph:
            for v, w in graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    affected.add(v)
    
    return affected
```

### Common Pitfalls
1. **Infinite Loop**: Always check for negative cycles
2. **Unreachable Vertices**: Handle inf distances properly
3. **Integer Overflow**: Use appropriate data types
4. **Graph Representation**: Ensure consistent edge format