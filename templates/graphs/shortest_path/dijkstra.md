# Dijkstra's Algorithm

Dijkstra's algorithm finds the shortest path from a source vertex to all other vertices in a weighted graph with non-negative edge weights.

## Algorithm Overview

1. **Initialize** distances to all vertices as infinity, except source (distance = 0)
2. **Use priority queue** to always process the vertex with minimum distance
3. **Relax edges**: For each neighbor, update distance if shorter path found
4. **Mark processed**: Once a vertex is processed, its shortest distance is final

## Core Implementation

```python
def dijkstra(graph, start):
    dist = defaultdict(lambda: float('inf'))
    dist[start] = 0
    pq = [(0, start)]
    
    while pq:
        d, u = heapq.heappop(pq)
        
        if d > dist[u]:  # Skip outdated entries
            continue
            
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:  # Relaxation
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    
    return dict(dist)
```

## Key Components

### Graph Representation
```python
graph = {
    node: [(neighbor, weight), ...]
}
```

### Priority Queue
- **Min-heap** to get vertex with minimum distance
- **Lazy deletion**: Skip outdated entries instead of decreasing keys
- **Entry format**: `(distance, vertex)`

### Relaxation Process
```python
if dist[u] + w < dist[v]:
    dist[v] = dist[u] + w
    heapq.heappush(pq, (dist[v], v))
```

## Path Reconstruction

```python
def dijkstra_with_path(graph, start, end=None):
    # ... same distance calculation ...
    parent = {}  # Track predecessors
    
    # During relaxation:
    if dist[u] + w < dist[v]:
        dist[v] = dist[u] + w
        parent[v] = u  # Record parent
        heapq.heappush(pq, (dist[v], v))
    
    # Reconstruct path
    path = []
    if end and end in parent:
        curr = end
        while curr != start:
            path.append(curr)
            curr = parent[curr]
        path.append(start)
        path.reverse()
    
    return dict(dist), path
```

## Example Walkthrough

**Graph:**
```
    0 ----4---- 1
    |           |
    1           1
    |           |
    2 ----2---- 3
         5
```

**Step-by-step execution from vertex 0:**

1. **Initialize**: `dist = {0: 0, others: ∞}`, `pq = [(0, 0)]`

2. **Process vertex 0**: 
   - Relax edges: `dist[1] = 4`, `dist[2] = 1`
   - `pq = [(1, 2), (4, 1)]`

3. **Process vertex 2** (distance 1):
   - Relax edges: `dist[1] = min(4, 1+2) = 3`, `dist[3] = 6`
   - `pq = [(3, 1), (4, 1), (6, 3)]`

4. **Process vertex 1** (distance 3):
   - Relax edges: `dist[3] = min(6, 3+1) = 4`
   - `pq = [(4, 1), (4, 3), (6, 3)]`

5. **Final distances**: `{0: 0, 1: 3, 2: 1, 3: 4}`

## Time Complexity

| Implementation | Time Complexity | Space Complexity |
|----------------|----------------|------------------|
| **Binary Heap** | **O((V + E) log V)** | **O(V)** |
| Fibonacci Heap | O(E + V log V) | O(V) |
| Array | O(V²) | O(V) |

### Analysis
- **V vertices, E edges**
- **Each vertex** added to heap once: O(V log V)
- **Each edge** relaxed at most once: O(E log V)
- **Total**: O((V + E) log V)

## Space Complexity

- **Distance array**: O(V)
- **Priority queue**: O(V) in worst case
- **Parent array** (for path): O(V)
- **Total**: O(V)

## Optimizations

### 1. Early Termination
```python
if u == target:
    break  # Found shortest path to target
```

### 2. Bidirectional Search
- Run Dijkstra from both source and target
- Stop when they meet in the middle
- **Time**: O(b^(d/2)) vs O(b^d)

### 3. A* Algorithm
- Use heuristic to guide search toward target
- **Heuristic**: h(n) ≤ actual distance to goal
- **Priority**: f(n) = g(n) + h(n)

## Common Pitfalls

1. **Negative weights**: Dijkstra fails with negative edges
2. **Forgetting lazy deletion**: Check `if d > dist[u]: continue`
3. **Wrong graph format**: Ensure `(neighbor, weight)` tuples
4. **Integer overflow**: Use appropriate data types for large weights

## Applications

### Shortest Path Problems
- **GPS Navigation**: Road networks with travel times
- **Network Routing**: Internet packet routing protocols
- **Game AI**: Pathfinding in games

### Beyond Shortest Paths
- **Social Networks**: Degrees of separation
- **Airline Routes**: Cheapest flight connections
- **Supply Chain**: Minimum cost distribution

## Variants

### Single-Source All-Destinations
```python
distances = dijkstra(graph, source)
```

### Single-Source Single-Destination
```python
distances, path = dijkstra_with_path(graph, source, target)
```

### All-Pairs Shortest Path
```python
all_distances = {}
for vertex in graph:
    all_distances[vertex] = dijkstra(graph, vertex)
```

## Comparison with Other Algorithms

| Algorithm | Use Case | Time | Negative Weights |
|-----------|----------|------|------------------|
| **Dijkstra** | Single-source, non-negative | O((V+E) log V) | ❌ |
| **Bellman-Ford** | Single-source, any weights | O(VE) | ✅ |
| **Floyd-Warshall** | All-pairs | O(V³) | ✅ |
| **A*** | Single-source with heuristic | O(b^d) | ❌ |

## Implementation Tips

1. **Use `defaultdict(lambda: float('inf'))`** for cleaner distance initialization
2. **Lazy deletion** is simpler than decrease-key operations
3. **Store `(distance, vertex)`** in heap for correct ordering
4. **Check graph connectivity** before running algorithm
5. **Handle edge cases**: empty graph, unreachable vertices