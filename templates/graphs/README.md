# Graph Algorithms Collection

A comprehensive collection of graph algorithms organized by category for competitive programming and algorithm study.

## 📁 Folder Structure

### 🛣️ **shortest_path/**
Algorithms for finding shortest paths between vertices.

- **`dijkstra.py`** - Single-source shortest path (non-negative weights)
  - Priority queue implementation with path reconstruction
  - **Use when**: Non-negative weights, single source, dense graphs
  - **Time**: O((V + E) log V), **Space**: O(V)

- **`bellman_ford.py`** - Single-source shortest path (handles negative weights)
  - Detects negative cycles, works with negative edge weights
  - **Use when**: Negative edges, negative cycle detection needed
  - **Time**: O(VE), **Space**: O(V)

- **`floyd_warshall.py`** - All-pairs shortest paths
  - Works with negative weights, simple implementation
  - **Use when**: Dense graphs, all-pairs distances, small graphs (V ≤ 500)
  - **Time**: O(V³), **Space**: O(V²)

- **`johnson.py`** - All-pairs shortest paths (sparse graphs)
  - Combines Bellman-Ford + Dijkstra, handles negative weights
  - **Use when**: Sparse graphs with negative edges, E << V²
  - **Time**: O(V² log V + VE), **Space**: O(V²)

### 🌳 **minimum_spanning_tree/**
Algorithms for finding minimum spanning trees.

- **`kruskal.py`** - MST using Union-Find (edge-based)
  - Greedy algorithm, works well with edge lists
  - **Use when**: Sparse graphs, edge-centric problems, Union-Find applications
  - **Time**: O(E log E), **Space**: O(V)

### 🔗 **connectivity/**
Algorithms for analyzing graph connectivity and structure.

- **`strongly_connected_components.py`** - SCC, Bridges, Articulation Points
  - Kosaraju's and Tarjan's algorithms for SCCs
  - Tarjan's algorithms for bridges and articulation points
  - **Use when**: Directed graph analysis, critical edge/vertex identification
  - **Time**: O(V + E), **Space**: O(V)

- **`cycle_detection.py`** - Detect cycles in directed/undirected graphs
  - DFS-based and Union-Find approaches
  - **Use when**: Dependency analysis, deadlock detection, DAG verification
  - **Time**: O(V + E), **Space**: O(V)

### ⭐ **special_properties/**
Algorithms for special graph properties and classifications.

- **`bipartite_check.py`** - Check if graph is bipartite
  - BFS/DFS coloring and Union-Find approaches
  - **Use when**: 2-coloring, matching problems, conflict resolution
  - **Time**: O(V + E), **Space**: O(V)

- **`topological_sort.py`** - Topological ordering of DAG
  - Kahn's algorithm (BFS) and DFS-based approaches
  - **Use when**: Dependency resolution, task scheduling, prerequisite ordering
  - **Time**: O(V + E), **Space**: O(V)

### 📊 **representations/**
Graph data structure representations.

- **`adjacency_list.py`** - Dynamic, memory-efficient representation
  - **Use when**: Sparse graphs, graph traversal, dynamic graphs
  - **Space**: O(V + E)

- **`adjacency_matrix.py`** - Fixed-size, fast edge queries
  - **Use when**: Dense graphs, frequent edge queries, small graphs
  - **Space**: O(V²)

## 🎯 Algorithm Selection Guide

### By Problem Type

#### **Single-Source Shortest Path**
- **Non-negative weights**: `dijkstra.py`
- **Negative weights**: `bellman_ford.py`
- **Unweighted**: BFS (simple case of Dijkstra)

#### **All-Pairs Shortest Path**
- **Dense graphs**: `floyd_warshall.py`
- **Sparse graphs**: `johnson.py` or multiple Dijkstra
- **No negative edges**: Multiple `dijkstra.py`

#### **Minimum Spanning Tree**
- **Sparse graphs**: `kruskal.py`
- **Dense graphs**: Prim's algorithm (not implemented)

#### **Graph Analysis**
- **Cycle detection**: `cycle_detection.py`
- **Bipartite check**: `bipartite_check.py`
- **Topological order**: `topological_sort.py`
- **Connected components**: `strongly_connected_components.py`

### By Graph Characteristics

#### **Sparse Graphs (E ≈ V)**
- Dijkstra, Kruskal, Johnson's, DFS-based algorithms

#### **Dense Graphs (E ≈ V²)**
- Floyd-Warshall, Prim's, adjacency matrix representation

#### **Directed Graphs**
- Topological sort, SCC algorithms, directed cycle detection

#### **Undirected Graphs**
- MST algorithms, undirected cycle detection, bipartite check

## 🚀 Quick Reference

### Time Complexities
| Algorithm | Time Complexity | Best For |
|-----------|----------------|----------|
| Dijkstra | O((V+E) log V) | Single-source, non-negative |
| Bellman-Ford | O(VE) | Negative edges, cycle detection |
| Floyd-Warshall | O(V³) | All-pairs, dense graphs |
| Johnson's | O(V² log V + VE) | All-pairs, sparse graphs |
| Kruskal | O(E log E) | MST, sparse graphs |
| Tarjan SCC | O(V + E) | Strongly connected components |
| Topological Sort | O(V + E) | DAG ordering |
| Bipartite Check | O(V + E) | 2-coloring |

### Space Complexities
- **Most algorithms**: O(V) auxiliary space
- **All-pairs algorithms**: O(V²) for distance matrix
- **Adjacency matrix**: O(V²) storage
- **Adjacency list**: O(V + E) storage

## 📝 Usage Notes

1. **All `.py` files contain clean implementations** without comments for competitive programming
2. **All `.md` files contain comprehensive documentation** with explanations, use cases, and examples
3. **Each algorithm includes multiple variants** and optimization techniques
4. **"Where & When to Use?" sections** help choose the right algorithm for your problem

## 🔧 Implementation Features

- **No external dependencies** - only standard library
- **Consistent interfaces** - similar function signatures across algorithms
- **Error handling** - proper handling of edge cases and invalid inputs
- **Path reconstruction** - available for shortest path algorithms
- **Multiple approaches** - different implementations for same problems