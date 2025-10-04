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

#define pans cout << ans << endl
#define pyes cout << "YES" << endl
#define pno cout << "NO" << endl
#define pm1 cout << -1 << endl
#define pvec(v) for (auto x : v) cout << x << " "; cout << "\n";

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

void solve() {

    // int n; cin >> n; vector<int> a(n); for (int i = 0; i < n; i++) cin >> a[i];

    int n, m; cin >> n >> m; vector<int> a(m, 0); for (int i = 0; i < m; i++) cin >> a[i];
    // int n, m; cin >> n >> m; vector<vector<int>> mat(n, vector<int>(m)); for(int i=0;i<n;i++) for(int j=0;j<m;j++) cin >> mat[i][j];

    sort(all(a));

    vector<int> gaps;

    for (int i = 0; i < m - 1; i++){
        int gap = a[i + 1] - a[i] - 1;
        if (gap > 0) gaps.push_back(gap);
    }

    int lastGap = (a[0] + n) - a[m - 1] - 1;
    if (lastGap > 0) gaps.push_back(lastGap);

    sort(all(gaps));
    reverse(all(gaps));

    int days = 0;
    int saved = 0;

    for (int gap : gaps) {
        
        int canBeAffected = gap - 2*days;
        int val = canBeAffected;

        if (val <= 0) {
            continue;
        }

        if (val == 1) {
            saved += 1;
            days += 1;
        } else {
            saved += (val - 1);
            days += 2;
        }
    }

    int ans = n - saved;

    pans;



}