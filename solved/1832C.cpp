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

    int n; cin >> n; vector<int> a(n); for (int i = 0; i < n; i++) cin >> a[i];

    // int n, k; cin >> n >> k; vector<int> a(n, 0); for (int i = 0; i < n; i++) cin >> a[i];

    int contrast = 0;

    for (int i = 1; i < n; i++) contrast += abs(a[i] - a[i - 1]);

    if (contrast == 0) {
        cout << 1 << "\n";
        return;
    }

    n = unique(a.begin(), a.end()) - a.begin();

    int ans = n;

    for (int i = 0; i < n - 2; ++i) {
        ans -= (a[i] < a[i + 1] && a[i + 1] < a[i + 2]);
        ans -= (a[i] > a[i + 1] && a[i + 1] > a[i + 2]);
    }

    cout << ans << "\n";

}