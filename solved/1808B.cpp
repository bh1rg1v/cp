#include <bits/stdc++.h>
using namespace std;

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

    // int n; cin >> n; vector<int> nums(n); for (int i = 0; i < n; i++) cin >> nums[i];

    // int n, m; cin >> n >> m; vector<int> nums(n, 0); for (int i = 0; i < n; i++) cin >> nums[i];


    int n, m; cin >> n >> m;
    vector<vector<int>> mat(n, vector<int>(m, 0)); for (int i = 0; i < n; i++) for (int j = 0; j < m; j++) cin >> mat[i][j];

    long long ans = 0;

    for (int j = 0; j < m; j++) {

        vector<int> col(n);
        for (int i = 0; i < n; i++) col[i] = mat[i][j];

        sort(col.begin(), col.end());


        for (int i = 0; i < n; i++) {
            ans += 1LL * col[i] * i - 1LL * col[i] * (n - i - 1);
        }
    }

    cout << ans << "\n";

}