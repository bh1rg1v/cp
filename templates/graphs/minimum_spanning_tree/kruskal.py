class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        
        self.components -= 1
        return True

def kruskal(edges, n):
    edges.sort(key=lambda x: x[2])
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

def kruskal_with_validation(edges, n):
    if not edges:
        return [], 0
    
    edges.sort(key=lambda x: x[2])
    uf = UnionFind(n)
    mst = []
    total_weight = 0
    
    for u, v, w in edges:
        if uf.union(u, v):
            mst.append((u, v, w))
            total_weight += w
    
    if len(mst) != n - 1:
        return None, None
    
    return mst, total_weight

def find_mst_edges_count(edges, n):
    edges.sort(key=lambda x: x[2])
    uf = UnionFind(n)
    count = 0
    
    for u, v, w in edges:
        if uf.union(u, v):
            count += 1
            if count == n - 1:
                break
    
    return count

def kruskal_maximum_spanning_tree(edges, n):
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