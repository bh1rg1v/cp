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

    int n, k;
    cin >> n >> k;

    vector<int> nums(n); for (int i = 0; i < n; i++) cin >> nums[i];

    BIT bit(nums, "sum");

    for (int i = 0; i < k; i++) {

        int type;
        cin >> type;

        if (type == 1){

            int idx, val; cin >> idx >> val;
            int diff = val - nums[idx - 1];
            nums[idx - 1] = val;

            bit.update(idx, diff);

        } else if (type == 2) {
    
            int l, r; cin >> l >> r;
            cout << bit.rangeQuery(l, r) << endl;

        }

    }
}

void solve() {

    int n; cin >> n; vector<int> a(n); for (int i = 0; i < n; i++) cin >> a[i];

    // int n, k; cin >> n >> k; vector<int> nums(n, 0); for (int i = 0; i < n; i++) cin >> nums[i];
    // int n, m; cin >> n >> m; vector<vector<int>> mat(n, vector<int>(m)); for(int i=0;i<n;i++) for(int j=0;j<m;j++) cin >> mat[i][j];


}