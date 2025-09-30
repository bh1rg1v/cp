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

    int n, k;
    cin >> n >> k;

    vector<int> colors(n, 0);

    for (int i = 0; i < n; i++) cin >> colors[i];

    vector<int> lastStep(k, -1);
    vector<int> maxStep(k), max2Step(k);

    for (int i = 0; i < n; i++) {
        int step = i - lastStep[colors[i] - 1];
        
        if (step > maxStep[colors[i] - 1]) {
            max2Step[colors[i] - 1] = maxStep[colors[i] - 1];
            maxStep[colors[i] - 1] = step;
        } else if (step > max2Step[colors[i] - 1]) {
            max2Step[colors[i] - 1] = step;
        }

        lastStep[colors[i] - 1] = i;
    }

    for (int i = 0; i < k; i++) {

        int step = n - lastStep[i];

        if (step > maxStep[i]) {
            max2Step[i] = maxStep[i];
            maxStep[i] = step;
        } else if (step > max2Step[i]) {
            max2Step[i] = step;
        };
    }

    int ans = 1e9;

    for (int i = 0; i < k; i++) {
        ans = min(ans, max((maxStep[i] + 1) / 2,max2Step[i]));
    }

    cout << ans - 1 << "\n";

}