
# Binary Search on Answer

def miniMax(nums, low, high):

    def isMidValid(mid):
        pass

    ans = high
    while low <= high:

        mid = (low + high) // 2

        if isMidValid(mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans

def maxiMin(nums, low, high):

    def isMidValid(mid):
        pass

    ans = low
    while low <= high:

        mid = (low + high) // 2

        if isMidValid(mid):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1

    return ans

# Trees

def preorder(root):
    if root == None:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)

def inorder(root):
    if root == None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)

def postorder(root):
    if root == None:
        return []
    return preorder(root.left) + preorder(root.right) + [root.val]

def morris(root):

    res = []

    while root != None:

        if root.left == None:
            res.append(root.val)
            root = root.right
        else:

            predec = root.left
            while predec.right and predec.right != root:
                predec = predec.right

            if predec.right == None:
                predec.right = root
                root = root.left
            else:
                predec.right = None
                res.append(root.val)
                root = root.right
    return res

from collections import deque
from math import *

def bfs(root):

    res = []
    queue = deque([root])

    while queue:

        n = len(queue)
        level = []

        for _ in range(n):

            node = queue.popleft()
            level.append(node.val)

            for nei in [node.left, node.right]:
                if nei:
                    queue.append(nei)

        res.append(level)

    return res

class BIT:

    def __init__(self, n, nums):
        self.bit = [0] * (n + 1)
        self.n = n

        for idx in range(n):
            self.update(idx, nums[idx])

    def update(self, idx, delta):

        idx += 1

        while idx <= self.n:
            self.bit[idx] += delta
            idx += idx & -idx

    def query(self, idx):

        idx += 1
        res = 0

        while idx > 0:
            res += self.bit[idx]
            idx -= idx & -idx

        return res

class SegmentTree:

    def __init__(self, nums):

        self.n = len(nums)
        self.seg = [0] * (4 * self.n)
        self.nums = nums
        self.build(1, 0, self.n - 1)

    def combine(self, left, right):
        return left + right
    
    def build(self, idx, left, right):

        if left == right:
            self.seg[idx] = self.nums[left]
            return
        
        mid = (left + right) // 2
        self.build(2 * idx, left, mid)
        self.build(2 * idx + 1, mid + 1, right)
        self.seg[idx] = self.combine(self.seg[2 * idx], self.seg[2 * idx + 1])

    def query(self, idx, left, right, ql, qr):
        
        if ql > right or qr < left:
            return  0
        
        if ql <= left and right <= qr:
            return self.seg[idx]
        
        mid = (left + right) // 2

        return self.combine(
            self.query(2 * idx, left, mid, ql, qr),
            self.query(2 * idx + 1, mid + 1, right, ql, qr)
        )
    
    def update(self, idx, left, right, pos, val):

        if left == right:
            self.seg[idx] = val
            return
        
        mid = (left + right) // 2

        if pos <= mid:
            self.update(2 * idx, left, mid, pos, val)
        else:
            self.update(2 * idx + 1, mid + 1, right, pos, val)

        self.seg[idx] = self.combine(self.seg[2 * idx], self.seg[2 * idx + 1])

class STLP:

    def __init__(self, nums):
        
        self.n = len(nums)
        self.nums = nums
        self.seg = [0] * (4 * self.n)
        self.lazy = [0] * (4 * self.n)

        self.build(1, 0, self.n - 1)

    def combine(self, left, right):
        return left + right

    def build(self, idx, left, right):

        if left == right:
            self.seg[idx] = self.nums[left]
            return
        
        mid = (left + right) // 2

        self.build(2 * idx, left, mid)
        self.build(2 * idx + 1, mid + 1, right)

        self.seg[idx] = self.combine(self.seg[2 * idx], self.seg[2 * idx + 1])

    def propagate(self, idx, left, right):

        if self.lazy[idx] != 0:

            self.seg[idx] += (right - left + 1) * self.lazy[idx]

            if left != right:
                self.lazy[2 * idx] += self.lazy[idx]
                self.lazy[2 * idx + 1] += self.lazy[idx]

            self.lazy[idx] = 0
    
    def query(self, idx, left, right, ql, qr):

        self.propagate(idx, left, right)

        if ql > right or qr < left:
            return 0
        
        if ql <= left and right <= qr:
            return self.seg[idx]
        
        mid = (left + right) // 2

        return self.combine(
            self.query(2 * idx, left, mid, ql, qr),
            self.query(2 * idx + 1, mid + 1, right, ql, qr)
        )
    
    def update(self, idx, left, right, ql, qr, val):

        self.propagate(idx, left, right)

        if ql > right or qr < left:
            return
        
        if ql <= left and right <= qr:
            self.lazy[idx] += val
            self.propagate(idx, left, right)
            return
        
        mid = (left + right) // 2

        self.update(2 * idx, left, mid, ql, qr, val)
        self.update(2 * idx + 1, mid + 1, right, ql, qr, val)

        self.seg[idx] = self.combine(self.seg[2 * idx], self.seg[2 * idx + 1])

    def range_query(self, left, right):
        return self.query(1, 0, self.n - 1, left, right)
    
    def range_update(self, left, right, val):
        self.update(1, 0, self.n - 1, left, right, val)

# Graphs

def dfs(graph, node, seen = None):

    if seen == None:
        seen = set()

    res = [node]
    seen.add(node)

    for nei in graph[node]:
        if nei not in seen:
            res.extend(dfs(graph, nei, seen))

    return res

def bfs(root, graph):

    res = []
    queue = deque([root])
    seen = set([root])

    while queue:
        node = queue.popleft()
        res.append(node)

        for nei in graph[node]:
            if nei not in seen:
                queue.append(nei)
                seen.add(nei)

    return res

from collections import defaultdict

def topoSort(edges, n, oneBased=0):

    graph = defaultdict(list)
    indegree = [0] * (n + oneBased)

    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1

    topo = []

    queue = deque([node for node in range(oneBased, n + oneBased) if indegree[node] == 0])

    while queue:
        node = queue.popleft()
        topo.append(node)

        for nei in graph[node]:
                
            indegree[nei] -= 1

            if indegree[nei] == 0:
                queue.append(nei)

    if len(topo) != n:
        return -1

    return topo

def isBipartite(graph, n):

    color = [-1] * n

    for start in range(n):

        if color[start] == -1:

            queue = deque([start])
            color[start] = 1

            while queue:

                node = queue.popleft()

                for nei in graph[node]:

                    if color[nei] == -1:
                        color[nei] = 1 - color[node]
                    elif color[nei] == color[node]:
                        return False

    return True

import heapq

def dijkstra(source, graph, n):

    dist = [float("inf")] * n

    queue = [(0, source)]
    dist[source] = 0

    while queue:

        d, u = heapq.heappop(queue)

        if d > dist[u]:
            continue

        for v, w in graph[u]:

            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(queue, (dist[v], v))

    return dist

def bellmanFord(source, graph, n):

    dist = [float("inf")] * n
    dist[source] = 0

    for _ in range(n - 1):
        for u in range(n):
            for v, w in graph[u]:
                if dist[u] != float("inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

    for u in range(n):
        for v, w in graph[u]:
            if dist[u] != float("inf") and dist[u] + w < dist[v]:
                return -1
            
    return dist

def floydWarshall(edges, n):

    dist = [[float("inf")] * n for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0

    for u, v, w in edges:
        dist[u][v] = min(dist[u][v], w)

    for k in range(n):
        for u in range(n):
            for v in range(n):
                if dist[u][k] != float("inf")  and dist[k][v] != float("inf"):
                    dist[u][v] = min(dist[u][v], dist[u][k] + dist[k][v])

    for i in range(n):
        if dist[i][i] < 0:
            return -1
        
    return dist

class DSU:

    def __init__(self, n):
        self.rank = [0] * n
        self.size = [1] * n
        self.parent = [node for node in range(n)]
        self.components = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)

        if px == py:
            return False
        
        if self.rank[py] < self.rank[px]:
            self.parent[py] = px
        elif self.rank[px] < self.rank[py]:
            self.parent[px] = py
        else:
            self.parent[py] = px
            self.rank[px] += 1
        
        self.components -= 1
        return True
    
def kruskal(edges, n):

    dsu = DSU(n)
    mst = []
    weight = 0

    minHeap = [(w, u, v) for u, v, w in edges]
    heapq.heapify(minHeap)

    while minHeap and len(mst) < n - 1:

        w, u, v = heapq.heappop(minHeap)

        if dsu.union(u, v):
            mst.append((u, v, w))
            weight += w

    if len(mst) != n - 1:
        return -1

    return mst, weight

def prims(graph, start = 0):

    mst = []
    seen = set()
    totalWeight = 0

    pq = [(0, start, -1)]

    while pq:
        weight, node, parent = heapq.heappop(pq)

        if node in seen:
            continue

        seen.add(node)

        if parent != -1:
            mst.append((parent, node, weight))
            totalWeight += weight

        for v, w in graph[node]:
            if v not in seen:
                heapq.heappush(pq, (w, v, node))

    return mst, totalWeight

def kosaraju(graph, n):
    
    seen = set()
    components = []
    finishingOrder = []

    def dfs(node):

        seen.add(node)

        for nei in graph[node]:
            if nei not in seen:
                dfs(nei)

        finishingOrder.append(node)

    for node in range(n):
        if node not in seen:
            dfs(node)

    transposed = defaultdict(list)

    for u in range(n):
        for v in graph[u]:
            transposed[v].append(u)

    seen.clear()

    def dfs2(node, comp):
        seen.add(node)
        comp.append(node)

        for nei in transposed[node]:
            if nei not in seen:
                dfs2(nei, comp)
    
    for node in reversed(finishingOrder):

        if node not in seen:
            comp = []
            dfs2(node, comp)
            components.append(comp)
    
    return components, len(components)

def tarjan(graph, n):

    def dfs(node, parent, visited, graph, tin, low, bridges, timer):

        visited.add(node)
        tin[node] = low[node] = timer
        timer[0] += 1

        for nei in graph[node]:

            if nei == parent:
                continue

            if nei not in visited:
                dfs(nei, node, visited, graph, tin, low, bridges, timer)
                low[node] = min(low[node], low[nei])

                if low[nei] > tin[node]:
                    bridges.append((node, nei))
            else:
                low[node] = min(low[node], tin[nei])


    bridges = []

    tin = [0] * n
    low = [0] * n
    timer = [1]
    visited = set()

    for i in range(n):
        if i not in visited:
            dfs(i, -1, visited, graph, tin, low, bridges, timer)

    return bridges

def articulationPoints(graph, n):

    def dfs(node, parent, graph, visited, low, tin, timer, ans):

        visited.add(node)
        tin[node] = low[node] = timer[0]
        timer[0] += 1
        child = 0

        for nei in graph[node]:

            if nei == parent:
                continue

            if nei not in visited:
                dfs(nei, node, graph, visited, low, tin, timer, ans)

                low[node] = min(low[node], low[nei])

                if low[nei] >= tin[node] and parent != -1:
                    ans.add(node)
                
                child += 1
            else:
                low[node] = min(low[node], tin[nei])

        if child > 1 and parent == -1:
            ans.add(node)

    ans = set()
    visited = set()
    low = [0] * n
    tin = [0] * n
    timer = [0]

    for node in range(n):
        if node not in visited:
            dfs(node, -1, graph, visited, low, tin, timer, ans)

    return list(ans) if ans else [-1]
