#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef vector<int> vi;
typedef vector<ll> vll;

const int INF = 1e9;
const ll LINF = 1e18;
const int MOD = 1e9+7;

#define pb push_back
#define mp make_pair
#define all(v) (v).begin(), (v).end()
#define ff first
#define ss second
#define sz(x) (int)(x).size()

#define pans cout << ans << endl
#define pyes cout << "YES" << endl
#define pno cout << "NO" << endl
#define pm1 cout << -1 << endl
#define pvec(v) for (auto x : v) cout << x << " "; cout << "\n";
#define int long long

#define MAX(v) (*max_element((v).begin(), (v).end()))
#define MIN(v) (*min_element((v).begin(), (v).end()))
#define SUM(v) accumulate((v).begin(), (v).end(), 0LL)

#define OFREQ(v) ([](auto &vec){ map<decltype(vec[0]), int> m; for (auto &x : vec) m[x]++; return m; }(v))
#define FREQ(v) ([](auto &vec){ unordered_map<decltype(vec[0]), int> m; for (auto &x : vec) m[x]++; return m; }(v))

#define OSET(v) (set<decltype(v[0])>(v.begin(), v.end()))
#define SET(v) (unordered_set<decltype(v[0])>(v.begin(), v.end()))

#define MAX_HEAP(T) priority_queue<T>
#define MIN_HEAP(T) priority_queue<T, vector<T>, greater<T>>

class BIT {
    int n;
    string mode;
    vector<long long> bit;

    long long combine(long long a, long long b) const {
        if (mode == "sum" || mode == "diff" || mode == "freq") return a + b;
        if (mode == "xor") return a ^ b;
        if (mode == "prod") return a * b;
        return 0;
    }

    long long inverse(long long a) const {
        if (mode == "sum" || mode == "diff" || mode == "freq") return -a;
        if (mode == "xor") return a;
        if (mode == "prod") return 1 / a; // careful, valid only for integers with mod inverse
        return 0;
    }

public:
    BIT(const vector<int>& nums, string modeType = "sum") {
        mode = modeType;
        n = nums.size();
        bit.assign(n + 1, (mode == "prod" ? 1 : 0));
        for (int i = 1; i <= n; ++i) update(i, nums[i - 1]);
    }

    void update(int idx, long long val) {
        while (idx <= n) {
            if (mode == "sum" || mode == "diff" || mode == "freq")
                bit[idx] += val;
            else if (mode == "xor")
                bit[idx] ^= val;
            else if (mode == "prod")
                bit[idx] *= val;
            idx += idx & -idx;
        }
    }

    long long query(int idx) const {
        long long res = (mode == "prod" ? 1 : 0);
        while (idx > 0) {
            if (mode == "sum" || mode == "diff" || mode == "freq")
                res += bit[idx];
            else if (mode == "xor")
                res ^= bit[idx];
            else if (mode == "prod")
                res *= bit[idx];
            idx -= idx & -idx;
        }
        return res;
    }

    long long rangeQuery(int left, int right) const {
        if (mode == "sum" || mode == "diff" || mode == "freq" || mode == "xor")
            return query(right) - query(left - 1);
        if (mode == "prod")
            return query(right) / query(left - 1);
        return 0;
    }
};

class SegmentTree {
    int n;
    string mode;
    vector<long long> seg;

    long long combine(long long a, long long b) const {
        if (mode == "sum") return a + b;
        if (mode == "min") return min(a, b);
        if (mode == "max") return max(a, b);
        if (mode == "xor") return a ^ b;
        return 0;
    }

    long long neutral() const {
        if (mode == "sum" || mode == "xor") return 0;
        if (mode == "min") return LLONG_MAX;
        if (mode == "max") return LLONG_MIN;
        return 0;
    }

    void build(const vector<int>& arr, int idx, int l, int r) {
        if (l == r) {
            seg[idx] = arr[l];
            return;
        }
        int mid = (l + r) / 2;
        build(arr, 2 * idx, l, mid);
        build(arr, 2 * idx + 1, mid + 1, r);
        seg[idx] = combine(seg[2 * idx], seg[2 * idx + 1]);
    }

    long long query(int idx, int l, int r, int ql, int qr) const {
        if (qr < l || ql > r) return neutral();
        if (ql <= l && r <= qr) return seg[idx];
        int mid = (l + r) / 2;
        return combine(
            query(2 * idx, l, mid, ql, qr),
            query(2 * idx + 1, mid + 1, r, ql, qr)
        );
    }

    void update(int idx, int l, int r, int pos, long long val) {
        if (l == r) {
            seg[idx] = val;
            return;
        }
        int mid = (l + r) / 2;
        if (pos <= mid) update(2 * idx, l, mid, pos, val);
        else update(2 * idx + 1, mid + 1, r, pos, val);
        seg[idx] = combine(seg[2 * idx], seg[2 * idx + 1]);
    }

public:
    SegmentTree(const vector<int>& arr, string modeType = "sum") {
        mode = modeType;
        n = arr.size();
        seg.assign(4 * n, 0);
        build(arr, 1, 0, n - 1);
    }

    long long query(int l, int r) const {
        return query(1, 0, n - 1, l, r);
    }

    void update(int pos, long long val) {
        update(1, 0, n - 1, pos, val);
    }
};

bool isMidValid(vector<int>& nums, int mid) {

        return true;

    }

int maxiMin(vector<int>& nums, int k) {

    int n = nums.size();

    int low = 0;
    int high = (int)1e9;

    while (low <= high) {

        int mid = low + (high - low) / 2;

        if (isMidValid(nums, mid)) low = mid;
        else high = mid - 1;
    }

    return low;
}

int miniMax(vector<int>& nums, int k) {

    int n = nums.size();
    int ans = -1;

    int low = 0;
    int high = (int)1e9;

    while (low <= high) {

        int mid = low + (high - low) / 2;

        if (isMidValid(nums, mid)) {
            ans = mid;
            high = mid + 1;
        } else {
            low = mid + 1;
        }

    }

    return high;
}

void solve();

int32_t main() {

    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    cin >> n >> q;

    vector<int> nums(n); for (int i = 0; i < n; i++) cin >> nums[i];

    SegmentTree st(nums, "min");

    for (int i = 0; i < q; i++) {

            int type;
            cin >> type;

            if (type == 1) {

                int pos, val; cin >> pos >> val;
                st.update(pos - 1, val);

            } else if (type == 2) {

                int l, r; cin >> l >> r; l--; r--;
                cout << st.query(l, r) << endl;
                
            }
        
    }

    return 0;
}

void solve() {

    int n; cin >> n; vector<int> a(n); for (int i = 0; i < n; i++) cin >> a[i];

    // int n, k; cin >> n >> k; vector<int> nums(n, 0); for (int i = 0; i < n; i++) cin >> nums[i];
    // int n, m; cin >> n >> m; vector<vector<int>> mat(n, vector<int>(m)); for(int i=0;i<n;i++) for(int j=0;j<m;j++) cin >> mat[i][j];


}