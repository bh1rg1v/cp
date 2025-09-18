# Topological Sort

Topological sorting is a linear ordering of vertices in a directed acyclic graph (DAG) such that for every directed edge (u,v), vertex u comes before v in the ordering.

## Algorithms

### 1. Kahn's Algorithm (BFS-based)
```python
def topological_sort_kahn(graph, n):
    indegree = [0] * n
    for u in graph:
        for v in graph[u]:
            indegree[v] += 1
    
    queue = deque()
    for i in range(n):
        if indegree[i] == 0:
            queue.append(i)
    
    result = []
    while queue:
        u = queue.popleft()
        result.append(u)
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)
    
    return result if len(result) == n else []
```

### 2. DFS-based Algorithm
```python
def topological_sort_dfs(graph, n):
    visited = [False] * n
    stack = []
    
    def dfs(u):
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                dfs(v)
        stack.append(u)
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
    
    return stack[::-1]
```

### 3. Cycle Detection + Topological Sort
```python
def has_cycle_dfs(graph, n):
    WHITE, GRAY, BLACK = 0, 1, 2
    color = [WHITE] * n
    
    def dfs(u):
        color[u] = GRAY
        for v in graph[u]:
            if color[v] == GRAY:
                return True
            if color[v] == WHITE and dfs(v):
                return True
        color[u] = BLACK
        return False
    
    for i in range(n):
        if color[i] == WHITE:
            if dfs(i):
                return True
    return False
```

## Complexity Analysis

| Algorithm | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| **Kahn's Algorithm** | **O(V + E)** | **O(V)** |
| **DFS-based** | **O(V + E)** | **O(V)** |
| **With Cycle Detection** | **O(V + E)** | **O(V)** |

## Where & When to Use?

### ✅ Use Topological Sort When:

#### Dependency Resolution
- **Build Systems**: Compile order for source files with dependencies
- **Package Managers**: Install packages in correct dependency order
- **Task Scheduling**: Execute tasks respecting prerequisites
- **Course Prerequisites**: Order courses based on requirements

#### Project Management
- **Critical Path Method**: Project task ordering
- **Gantt Charts**: Timeline creation with dependencies
- **Resource Planning**: Allocate resources in dependency order
- **Workflow Management**: Process step sequencing

#### Compiler Design
- **Symbol Resolution**: Process declarations before usage
- **Code Generation**: Generate code in dependency order
- **Optimization Passes**: Apply optimizations in correct sequence
- **Linking**: Link object files respecting dependencies

#### Database Systems
- **Query Optimization**: Join order optimization
- **Transaction Processing**: Serialize conflicting transactions
- **Schema Migration**: Apply database changes in order
- **Constraint Checking**: Validate foreign key dependencies

### Algorithm Choice Guidelines:

#### Use Kahn's Algorithm When:
- **Need to detect cycles** during sorting
- **Want iterative approach** (no recursion stack limits)
- **Processing nodes level by level** is beneficial
- **Memory usage is critical** (no recursion overhead)

#### Use DFS-based When:
- **Recursive solution is natural**
- **Need to process in reverse finish time order**
- **Simpler implementation preferred**
- **Part of larger DFS-based algorithm**

## Real-World Applications

### Software Engineering
- **Makefile Dependencies**: Build targets in correct order
- **Module Loading**: Import modules respecting dependencies
- **Plugin Systems**: Load plugins based on dependencies
- **Configuration Management**: Apply configs in dependency order

### Academic Systems
- **Course Scheduling**: Semester planning with prerequisites
- **Research Dependencies**: Paper citation ordering
- **Curriculum Design**: Subject sequence planning
- **Degree Requirements**: Course completion tracking

### Manufacturing
- **Assembly Line**: Component assembly order
- **Supply Chain**: Production scheduling with material dependencies
- **Quality Control**: Testing sequence with dependencies
- **Inventory Management**: Stock replenishment ordering

### Data Processing
- **ETL Pipelines**: Data transformation step ordering
- **Machine Learning**: Feature engineering pipeline
- **Data Validation**: Validation rule application order
- **Report Generation**: Report section dependencies

## Common Patterns

### Problem Recognition
Look for these keywords:
- **Dependencies/Prerequisites**
- **Ordering with constraints**
- **Before/After relationships**
- **Directed acyclic graph (DAG)**
- **Scheduling with dependencies**

### Implementation Considerations
1. **Cycle Detection**: Always check if graph is DAG first
2. **Multiple Valid Orders**: Topological sort may not be unique
3. **Empty Result**: Indicates cycle in graph
4. **Disconnected Components**: Handle isolated vertices

### Edge Cases
- **Empty graph**: Empty topological order
- **Single vertex**: Single element order
- **No edges**: Any order is valid
- **Cycles**: No valid topological order exists
- **Self-loops**: Creates cycle, no valid order

### Optimization Tips
- **Early Cycle Detection**: Use Kahn's algorithm for built-in detection
- **Memory Optimization**: Use DFS for lower memory usage
- **Parallel Processing**: Some nodes can be processed simultaneously
- **Incremental Updates**: Maintain topological order with dynamic changes

## Variations and Extensions

### Lexicographically Smallest Order
```python
# Use priority queue instead of regular queue in Kahn's
import heapq
pq = []
for i in range(n):
    if indegree[i] == 0:
        heapq.heappush(pq, i)
```

### All Topological Orders
```python
# Backtracking to find all possible orders
def all_topological_sorts(graph, n):
    # Implementation using backtracking
    pass
```

### Longest Path in DAG
- Topological sort enables O(V + E) longest path computation
- Useful for critical path analysis and scheduling

### Minimum Number of Semesters
- Find minimum levels needed to complete all courses
- Each level contains courses with no dependencies on later levels