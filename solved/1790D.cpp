#include <bits/stdc++.h>
using namespace std;

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

    int n; cin >> n; vector<int> nums(n); for (int i = 0; i < n; i++) cin >> nums[i];
    // int n, k; cin >> n >> k; vector<int> nums(n, 0); for (int i = 0; i < n; i++) cin >> nums[i];

    map<int, int> freq;
    set<int> s;

    for (int x : nums) {
        freq[x]++;
        s.insert(x);
    }

    int last = 0;
    int ans = 0;

    for (int num : s) {
        ans += max(0, freq[num] - freq[num - 1]);
        last = num;
    }

    cout << ans << endl;

}