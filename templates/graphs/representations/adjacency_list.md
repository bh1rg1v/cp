# Adjacency List Representation

An adjacency list represents a graph as a collection of lists, where each vertex stores a list of its adjacent vertices.

## Structure

```python
graph = {
    vertex: [(neighbor1, weight1), (neighbor2, weight2), ...]
}
```

## Implementation

```python
class AdjacencyList:
    def __init__(self, directed=False):
        self.graph = defaultdict(list)
        self.directed = directed
    
    def add_edge(self, u, v, weight=1):
        self.graph[u].append((v, weight))
        if not self.directed:
            self.graph[v].append((u, weight))
```

## Operations Complexity

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| **Add Edge** | **O(1)** | O(1) |
| **Remove Edge** | **O(degree)** | O(1) |
| **Check Edge** | **O(degree)** | O(1) |
| **Get Neighbors** | **O(1)** | O(degree) |
| **Space Total** | **O(V + E)** | - |

## Memory Usage

- **Space**: O(V + E) where V = vertices, E = edges
- **Each vertex**: Stores only its actual neighbors
- **Efficient**: No wasted space for non-existent edges

## Advantages

### Memory Efficient
- **Sparse graphs**: Only stores existing edges
- **Dynamic size**: Grows with actual edges, not potential edges
- **No wasted space**: Perfect for graphs with few edges

### Fast Iteration
- **Neighbor traversal**: O(degree) to visit all neighbors
- **DFS/BFS**: Optimal for graph traversal algorithms
- **Dynamic graphs**: Easy to add/remove vertices and edges

### Flexible Structure
- **Variable vertex count**: No need to pre-define graph size
- **Weighted edges**: Easy to store edge weights
- **Multiple edges**: Can handle multigraphs naturally

## Disadvantages

### Slower Edge Queries
- **Edge existence**: O(degree) to check if edge exists
- **Not constant time**: Must scan neighbor list
- **Worst case**: O(V) for complete graphs

### Cache Performance
- **Scattered memory**: Neighbors stored in different locations
- **Pointer chasing**: Following links reduces cache efficiency
- **Memory fragmentation**: Dynamic allocation overhead

## When to Use Adjacency Lists

### ✅ Ideal For:

#### Sparse Graphs
- **Social networks**: Most people know relatively few others
- **Web graphs**: Pages link to small subset of all pages
- **Road networks**: Intersections connect to few other intersections

#### Graph Traversal Algorithms
- **DFS/BFS**: Need to iterate through neighbors efficiently
- **Shortest path**: Dijkstra, Bellman-Ford benefit from fast neighbor access
- **Topological sort**: Requires efficient neighbor iteration

#### Dynamic Graphs
- **Streaming data**: Edges added/removed frequently
- **Interactive applications**: User modifies graph structure
- **Growing graphs**: Size unknown at initialization

#### Memory-Constrained Environments
- **Large sparse graphs**: Millions of vertices, few edges each
- **Mobile applications**: Limited memory availability
- **Embedded systems**: Memory optimization critical

### ❌ Avoid When:

#### Dense Graphs
- **Complete graphs**: Every vertex connected to every other
- **Near-complete graphs**: Most possible edges exist
- **Matrix operations**: Need to check many edge existences

#### Frequent Edge Queries
- **Edge weight lookups**: Constant-time access needed
- **Graph algorithms**: Require fast edge existence checks
- **Adjacency testing**: Primary operation is "is there an edge?"

## Example Use Cases

### Social Network Analysis
```python
# Friend connections (sparse, dynamic)
friends = AdjacencyList()
friends.add_edge("Alice", "Bob")
friends.add_edge("Bob", "Charlie")

# Efficient friend recommendation algorithms
def mutual_friends(person1, person2):
    friends1 = set(f for f, _ in friends.get_neighbors(person1))
    friends2 = set(f for f, _ in friends.get_neighbors(person2))
    return friends1 & friends2
```

### Web Crawling
```python
# Website link structure
web_graph = AdjacencyList(directed=True)
web_graph.add_edge("page1.html", "page2.html")
web_graph.add_edge("page1.html", "page3.html")

# Efficient crawling - follow outbound links
def crawl_from(start_page):
    for next_page, _ in web_graph.get_neighbors(start_page):
        process_page(next_page)
```

### Route Planning
```python
# City road network (sparse, weighted)
roads = AdjacencyList()
roads.add_edge("CityA", "CityB", 150)  # 150km
roads.add_edge("CityB", "CityC", 200)

# Efficient for pathfinding algorithms
def find_shortest_path(start, end):
    return dijkstra(roads.graph, start, end)
```

## Implementation Variants

### Simple List (Unweighted)
```python
graph = {
    0: [1, 2, 3],
    1: [0, 3],
    2: [0],
    3: [0, 1]
}
```

### List of Tuples (Weighted)
```python
graph = {
    0: [(1, 5), (2, 3)],
    1: [(3, 2)],
    2: [(1, 1), (3, 4)]
}
```

### Dictionary of Sets (Fast Lookup)
```python
graph = {
    0: {1, 2, 3},
    1: {0, 3},
    2: {0}
}
# O(1) edge existence check with sets
```

## Performance Comparison

### vs Adjacency Matrix

| Aspect | Adjacency List | Adjacency Matrix |
|--------|----------------|------------------|
| **Space** | O(V + E) | O(V²) |
| **Add Edge** | O(1) | O(1) |
| **Check Edge** | O(degree) | O(1) |
| **Iterate Neighbors** | O(degree) | O(V) |
| **Best For** | Sparse graphs | Dense graphs |

### Real-World Performance

#### Sparse Graph (V=10000, E=20000)
- **Adjacency List**: ~240KB memory
- **Adjacency Matrix**: ~400MB memory
- **Ratio**: 1600x more memory efficient

#### Dense Graph (V=1000, E=500000)
- **Adjacency List**: ~8MB memory  
- **Adjacency Matrix**: ~4MB memory
- **Matrix wins**: But edge queries much faster

## Best Practices

### Memory Optimization
```python
# Use appropriate data structures
from collections import defaultdict

# For unweighted graphs
graph = defaultdict(set)  # Fast edge lookup

# For weighted graphs  
graph = defaultdict(list)  # Store (neighbor, weight) tuples
```

### Performance Tips
1. **Pre-allocate**: Use `defaultdict` to avoid key errors
2. **Sort neighbors**: For consistent iteration order
3. **Use sets**: When only checking edge existence matters
4. **Compress vertices**: Map string vertices to integers for better performance

### Common Patterns
```python
# Efficient neighbor iteration
for neighbor, weight in graph[vertex]:
    process_edge(vertex, neighbor, weight)

# Safe edge checking
if vertex in graph and neighbor in dict(graph[vertex]):
    # Edge exists
    
# Degree calculation
degree = len(graph[vertex])
```