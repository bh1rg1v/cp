#include <bits/stdc++.h>
using namespace std;

// Binary Search
int binarySearch(vector<int>& arr, int target) {
    int low = 0, high = arr.size() - 1;
    
    while (low <= high) {
        int mid = low + (high - low) / 2;
        
        if (arr[mid] == target) return mid;
        else if (arr[mid] < target) low = mid + 1;
        else high = mid - 1;
    }
    
    return -1;
}

int binarySearchAnswer(int low, int high, function<bool(int)> isMidValid) {
    int ans = -1;
    
    while (low <= high) {
        int mid = low + (high - low) / 2;
        
        if (isMidValid(mid)) {
            ans = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    
    return ans;
}

// Tree Node Structure
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

// Tree Traversals
void preorder(TreeNode* root, vector<int>& res) {
    if (!root) return;
    res.push_back(root->val);
    preorder(root->left, res);
    preorder(root->right, res);
}

void inorder(TreeNode* root, vector<int>& res) {
    if (!root) return;
    inorder(root->left, res);
    res.push_back(root->val);
    inorder(root->right, res);
}

void postorder(TreeNode* root, vector<int>& res) {
    if (!root) return;
    postorder(root->left, res);
    postorder(root->right, res);
    res.push_back(root->val);
}

vector<int> morris(TreeNode* root) {
    vector<int> res;
    
    while (root) {
        if (!root->left) {
            res.push_back(root->val);
            root = root->right;
        } else {
            TreeNode* pred = root->left;
            while (pred->right && pred->right != root) {
                pred = pred->right;
            }
            
            if (!pred->right) {
                pred->right = root;
                root = root->left;
            } else {
                pred->right = nullptr;
                res.push_back(root->val);
                root = root->right;
            }
        }
    }
    
    return res;
}

vector<vector<int>> bfsTree(TreeNode* root) {
    vector<vector<int>> res;
    if (!root) return res;
    
    queue<TreeNode*> q;
    q.push(root);
    
    while (!q.empty()) {
        int n = q.size();
        vector<int> level;
        
        for (int i = 0; i < n; i++) {
            TreeNode* node = q.front();
            q.pop();
            level.push_back(node->val);
            
            if (node->left) q.push(node->left);
            if (node->right) q.push(node->right);
        }
        
        res.push_back(level);
    }
    
    return res;
}

// Binary Indexed Tree
class BIT {
public:
    vector<int> bit;
    int n;
    
    BIT(int size, vector<int>& nums) : n(size) {
        bit.assign(n + 1, 0);
        for (int i = 0; i < n; i++) {
            update(i, nums[i]);
        }
    }
    
    void update(int idx, int delta) {
        idx++;
        while (idx <= n) {
            bit[idx] += delta;
            idx += idx & -idx;
        }
    }
    
    int query(int idx) {
        idx++;
        int res = 0;
        while (idx > 0) {
            res += bit[idx];
            idx -= idx & -idx;
        }
        return res;
    }
};

// Segment Tree
class SegmentTree {
public:
    vector<int> seg, nums;
    int n;
    
    SegmentTree(vector<int>& arr) : nums(arr), n(arr.size()) {
        seg.assign(4 * n, 0);
        build(1, 0, n - 1);
    }
    
    int combine(int left, int right) {
        return left + right;
    }
    
    void build(int idx, int left, int right) {
        if (left == right) {
            seg[idx] = nums[left];
            return;
        }
        
        int mid = (left + right) / 2;
        build(2 * idx, left, mid);
        build(2 * idx + 1, mid + 1, right);
        seg[idx] = combine(seg[2 * idx], seg[2 * idx + 1]);
    }
    
    int query(int idx, int left, int right, int ql, int qr) {
        if (ql > right || qr < left) return 0;
        if (ql <= left && right <= qr) return seg[idx];
        
        int mid = (left + right) / 2;
        return combine(
            query(2 * idx, left, mid, ql, qr),
            query(2 * idx + 1, mid + 1, right, ql, qr)
        );
    }
    
    void update(int idx, int left, int right, int pos, int val) {
        if (left == right) {
            seg[idx] = val;
            return;
        }
        
        int mid = (left + right) / 2;
        if (pos <= mid) {
            update(2 * idx, left, mid, pos, val);
        } else {
            update(2 * idx + 1, mid + 1, right, pos, val);
        }
        
        seg[idx] = combine(seg[2 * idx], seg[2 * idx + 1]);
    }
};

// Segment Tree with Lazy Propagation
class STLP {
public:
    vector<long long> seg, lazy, nums;
    int n;
    
    STLP(vector<int>& arr) : nums(arr.begin(), arr.end()), n(arr.size()) {
        seg.assign(4 * n, 0);
        lazy.assign(4 * n, 0);
        build(1, 0, n - 1);
    }
    
    long long combine(long long left, long long right) {
        return left + right;
    }
    
    void build(int idx, int left, int right) {
        if (left == right) {
            seg[idx] = nums[left];
            return;
        }
        
        int mid = (left + right) / 2;
        build(2 * idx, left, mid);
        build(2 * idx + 1, mid + 1, right);
        seg[idx] = combine(seg[2 * idx], seg[2 * idx + 1]);
    }
    
    void propagate(int idx, int left, int right) {
        if (lazy[idx] != 0) {
            seg[idx] += (right - left + 1) * lazy[idx];
            
            if (left != right) {
                lazy[2 * idx] += lazy[idx];
                lazy[2 * idx + 1] += lazy[idx];
            }
            
            lazy[idx] = 0;
        }
    }
    
    long long query(int idx, int left, int right, int ql, int qr) {
        propagate(idx, left, right);
        
        if (ql > right || qr < left) return 0;
        if (ql <= left && right <= qr) return seg[idx];
        
        int mid = (left + right) / 2;
        return combine(
            query(2 * idx, left, mid, ql, qr),
            query(2 * idx + 1, mid + 1, right, ql, qr)
        );
    }
    
    void update(int idx, int left, int right, int ql, int qr, int val) {
        propagate(idx, left, right);
        
        if (ql > right || qr < left) return;
        
        if (ql <= left && right <= qr) {
            lazy[idx] += val;
            propagate(idx, left, right);
            return;
        }
        
        int mid = (left + right) / 2;
        update(2 * idx, left, mid, ql, qr, val);
        update(2 * idx + 1, mid + 1, right, ql, qr, val);
        
        propagate(2 * idx, left, mid);
        propagate(2 * idx + 1, mid + 1, right);
        seg[idx] = combine(seg[2 * idx], seg[2 * idx + 1]);
    }
    
    long long rangeQuery(int left, int right) {
        return query(1, 0, n - 1, left, right);
    }
    
    void rangeUpdate(int left, int right, int val) {
        update(1, 0, n - 1, left, right, val);
    }
};

// Graph Algorithms
void dfs(vector<vector<int>>& graph, int node, vector<bool>& visited, vector<int>& res) {
    visited[node] = true;
    res.push_back(node);
    
    for (int nei : graph[node]) {
        if (!visited[nei]) {
            dfs(graph, nei, visited, res);
        }
    }
}

vector<int> bfsGraph(int root, vector<vector<int>>& graph) {
    vector<int> res;
    queue<int> q;
    set<int> seen;
    
    q.push(root);
    seen.insert(root);
    
    while (!q.empty()) {
        int node = q.front();
        q.pop();
        res.push_back(node);
        
        for (int nei : graph[node]) {
            if (seen.find(nei) == seen.end()) {
                q.push(nei);
                seen.insert(nei);
            }
        }
    }
    
    return res;
}

vector<int> topoSort(vector<pair<int, int>>& edges, int n) {
    vector<vector<int>> graph(n);
    vector<int> indegree(n, 0);
    
    for (auto& edge : edges) {
        graph[edge.first].push_back(edge.second);
        indegree[edge.second]++;
    }
    
    vector<int> topo;
    queue<int> q;
    
    for (int i = 0; i < n; i++) {
        if (indegree[i] == 0) {
            q.push(i);
        }
    }
    
    while (!q.empty()) {
        int node = q.front();
        q.pop();
        topo.push_back(node);
        
        for (int nei : graph[node]) {
            indegree[nei]--;
            if (indegree[nei] == 0) {
                q.push(nei);
            }
        }
    }
    
    if (topo.size() != n) return {};
    return topo;
}

bool isBipartite(vector<vector<int>>& graph, int n) {
    vector<int> color(n, -1);
    
    for (int start = 0; start < n; start++) {
        if (color[start] == -1) {
            queue<int> q;
            q.push(start);
            color[start] = 1;
            
            while (!q.empty()) {
                int node = q.front();
                q.pop();
                
                for (int nei : graph[node]) {
                    if (color[nei] == -1) {
                        color[nei] = 1 - color[node];
                        q.push(nei);
                    } else if (color[nei] == color[node]) {
                        return false;
                    }
                }
            }
        }
    }
    
    return true;
}

vector<int> dijkstra(int source, vector<vector<pair<int, int>>>& graph, int n) {
    vector<int> dist(n, INT_MAX);
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    
    dist[source] = 0;
    pq.push({0, source});
    
    while (!pq.empty()) {
        int d = pq.top().first;
        int u = pq.top().second;
        pq.pop();
        
        if (d > dist[u]) continue;
        
        for (auto& edge : graph[u]) {
            int v = edge.first;
            int w = edge.second;
            
            if (dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                pq.push({dist[v], v});
            }
        }
    }
    
    return dist;
}

vector<int> bellmanFord(int source, vector<vector<pair<int, int>>>& graph, int n) {
    vector<int> dist(n, INT_MAX);
    dist[source] = 0;
    
    for (int i = 0; i < n - 1; i++) {
        for (int u = 0; u < n; u++) {
            if (dist[u] != INT_MAX) {
                for (auto& edge : graph[u]) {
                    int v = edge.first;
                    int w = edge.second;
                    if (dist[u] + w < dist[v]) {
                        dist[v] = dist[u] + w;
                    }
                }
            }
        }
    }
    
    for (int u = 0; u < n; u++) {
        if (dist[u] != INT_MAX) {
            for (auto& edge : graph[u]) {
                int v = edge.first;
                int w = edge.second;
                if (dist[u] + w < dist[v]) {
                    return {};
                }
            }
        }
    }
    
    return dist;
}

vector<vector<int>> floydWarshall(vector<tuple<int, int, int>>& edges, int n) {
    vector<vector<int>> dist(n, vector<int>(n, INT_MAX));
    
    for (int i = 0; i < n; i++) {
        dist[i][i] = 0;
    }
    
    for (auto& edge : edges) {
        int u = get<0>(edge);
        int v = get<1>(edge);
        int w = get<2>(edge);
        dist[u][v] = min(dist[u][v], w);
    }
    
    for (int k = 0; k < n; k++) {
        for (int u = 0; u < n; u++) {
            for (int v = 0; v < n; v++) {
                if (dist[u][k] != INT_MAX && dist[k][v] != INT_MAX) {
                    dist[u][v] = min(dist[u][v], dist[u][k] + dist[k][v]);
                }
            }
        }
    }
    
    for (int i = 0; i < n; i++) {
        if (dist[i][i] < 0) {
            return {};
        }
    }
    
    return dist;
}

// Disjoint Set Union
class DSU {
public:
    vector<int> parent, rank, size;
    int components;
    
    DSU(int n) : components(n) {
        parent.resize(n);
        rank.assign(n, 0);
        size.assign(n, 1);
        iota(parent.begin(), parent.end(), 0);
    }
    
    int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }
    
    bool unite(int x, int y) {
        int px = find(x), py = find(y);
        if (px == py) return false;
        
        if (rank[px] < rank[py]) swap(px, py);
        
        parent[py] = px;
        if (rank[px] == rank[py]) rank[px]++;
        
        components--;
        return true;
    }
    
    bool uniteBySize(int x, int y) {
        int px = find(x), py = find(y);
        if (px == py) return false;
        
        if (size[px] < size[py]) swap(px, py);
        
        parent[py] = px;
        size[px] += size[py];
        
        components--;
        return true;
    }
    
    int getSize(int x) {
        return size[find(x)];
    }
    
    bool connected(int x, int y) {
        return find(x) == find(y);
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    return 0;
}