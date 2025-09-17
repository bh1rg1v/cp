# Bipartite Graph Check

A bipartite graph is a graph whose vertices can be divided into two disjoint sets such that no two vertices within the same set are adjacent.

## Algorithms

### 1. BFS + Coloring
```python
def is_bipartite_bfs(graph):
    color = {}
    for start in graph:
        if start in color:
            continue
        queue = deque([start])
        color[start] = 0
        while queue:
            u = queue.popleft()
            for v in graph[u]:
                if v not in color:
                    color[v] = 1 - color[u]
                    queue.append(v)
                elif color[v] == color[u]:
                    return False
    return True
```

### 2. DFS + Coloring
```python
def is_bipartite_dfs(graph):
    color = {}
    def dfs(u, c):
        color[u] = c
        for v in graph[u]:
            if v not in color:
                if not dfs(v, 1 - c):
                    return False
            elif color[v] == color[u]:
                return False
        return True
    
    for start in graph:
        if start not in color:
            if not dfs(start, 0):
                return False
    return True
```

### 3. Union-Find Approach
```python
def is_bipartite_union_find(edges, n):
    uf = UnionFind(2 * n)
    for u, v in edges:
        if uf.find(u) == uf.find(v) or uf.find(u + n) == uf.find(v + n):
            return False
        uf.union(u, v + n)
        uf.union(u + n, v)
    return True
```

## Complexity Analysis

| Algorithm | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| **BFS Coloring** | **O(V + E)** | **O(V)** |
| **DFS Coloring** | **O(V + E)** | **O(V)** |
| **Union-Find** | **O(E α(V))** | **O(V)** |

## Where & When to Use?

### ✅ Use Bipartite Check When:

#### Graph Matching Problems
- **Maximum Bipartite Matching**: Need to verify graph is bipartite first
- **Assignment Problems**: Workers to tasks, students to projects
- **Stable Marriage**: Matching between two distinct groups

#### Conflict Resolution
- **Graph Coloring**: Check if 2-colorable (bipartite = 2-colorable)
- **Scheduling**: Two time slots, no conflicts between connected items
- **Resource Allocation**: Two types of resources, constraints between them

#### Network Analysis
- **Social Networks**: Users vs Pages, Authors vs Papers
- **Recommendation Systems**: Users vs Items bipartite graphs
- **Web Analysis**: Queries vs Documents, Advertisers vs Keywords

#### Competitive Programming
- **Contest Problems**: Often disguised as coloring or grouping problems
- **Optimization**: Many problems reduce to bipartite matching
- **Verification**: Check if solution exists before complex algorithms

### Algorithm Choice Guidelines:

#### Use BFS Coloring When:
- **Simple implementation needed**
- **Level-by-level processing preferred**
- **Iterative approach required** (avoid recursion limits)

#### Use DFS Coloring When:
- **Recursive solution is natural**
- **Need to track path information**
- **Memory usage is not critical**

#### Use Union-Find When:
- **Dynamic edge additions** (online algorithm)
- **Need to track connected components**
- **Part of larger Union-Find based solution**

## Real-World Applications

### Computer Science
- **Compiler Design**: Register allocation with interference graphs
- **Database Systems**: Query optimization with join graphs
- **Operating Systems**: Process scheduling with resource conflicts

### Mathematics
- **Graph Theory**: Fundamental property testing
- **Combinatorial Optimization**: Prerequisite for matching algorithms
- **Linear Programming**: Constraint satisfaction problems

### Industry Applications
- **Recommendation Engines**: User-item bipartite graphs
- **Social Media**: User-content interaction analysis
- **E-commerce**: Customer-product relationship modeling
- **Transportation**: Route planning with vehicle-road restrictions

## Common Patterns

### Problem Recognition
Look for these keywords:
- **Two groups/types** of entities
- **No connections within groups**
- **Alternating assignment**
- **2-coloring possible**
- **Matching between sets**

### Implementation Tips
1. **Choose appropriate representation**: Adjacency list vs edge list
2. **Handle disconnected components**: Check all vertices
3. **Early termination**: Return false as soon as conflict found
4. **Color assignment**: Use 0/1 or any two distinct values

### Edge Cases
- **Empty graph**: Always bipartite
- **Single vertex**: Always bipartite  
- **No edges**: Always bipartite
- **Self-loops**: Never bipartite (if allowed)
- **Disconnected graph**: Check each component separately