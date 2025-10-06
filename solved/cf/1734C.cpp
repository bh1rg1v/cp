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
#define f first
#define s second
#define sz(x) (int)(x).size()

#define MAX(v) (*max_element((v).begin(), (v).end()))
#define MIN(v) (*min_element((v).begin(), (v).end()))

#define OFREQ(v) ([](auto &vec){ map<decltype(vec[0]), int> m; for (auto &x : vec) m[x]++; return m; }(v))
#define FREQ(v) ([](auto &vec){ unordered_map<decltype(vec[0]), int> m; for (auto &x : vec) m[x]++; return m; }(v))

#define OSET(v) (set<decltype(v[0])>(v.begin(), v.end()))
#define SET(v) (unordered_set<decltype(v[0])>(v.begin(), v.end()))

#define MAX_HEAP(T) priority_queue<T>
#define MIN_HEAP(T) priority_queue<T, vector<T>, greater<T>>

bool isMidValid(vector<int>& nums, int mid) {

        return true;

    }

int maxiMin(vector<int>& nums, int k) {

    int n = nums.size();

    int low = 0;
    int high = int(1e9);

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
    int high = int(1e9);

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

int main() {

    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--) solve();

    return 0;
}

int upbound(vector<int>& ma, int q) {

    int idx = -1;
    int n = ma.size();

    int low = 0, high = n - 1;

    while (low <= high) {

        int mid = (low + high) / 2;

        if (ma[mid] <= q) {
            low = mid + 1;
        } else {
            idx = mid;
            high = mid - 1;
        }
    }

    return idx;
}

const int N = 1e6 + 1;
vector<int> minDivisors(N, -1);

void buildminDiv() {
    minDivisors[1] = 1;
    for (int i = 2; i < N; i++) {
        if (minDivisors[i] == -1) {
            minDivisors[i] = i;
            for (long long j = 1LL * i * i; j < N; j += i) {
                if (minDivisors[j] == -1) {
                    minDivisors[j] = i;
                }
            }
        }
    }
}

void solve() {

    // int n; cin >> n; vector<int> nums(n); for (int i = 0; i < n; i++) cin >> nums[i];

    // int n, k; cin >> n >> k; vector<int> nums(n, 0); for (int i = 0; i < n; i++) cin >> nums[i];
    // int n, m; cin >> n >> m; vector<vector<int>> mat(n, vector<int>(m)); for(int i=0;i<n;i++) for(int j=0;j<m;j++) cin >> mat[i][j];

    int n;
    cin >> n;

    bool a[n + 1];

    string str;
    cin >> str;

    for (int i = 1; i <= n; i++){
        a[i] = (str[i - 1] == '1');
    }

    int cost[n + 1];
    for (int i = n; i >= 1; i--){
        for (int j = i; j <= n; j += i){

            if (a[j]) break;
            cost[j] = i;

        }
    }

    ll ans = 0;

    for (int i = 1; i <= n; i++) {
        if (!a[i]) ans += cost[i];
    }

    cout << ans << endl;
}