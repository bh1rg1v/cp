#include <bits/stdc++.h>
using namespace std;

#define MAX(v) (*max_element((v).begin(), (v).end()))
#define MIN(v) (*min_element((v).begin(), (v).end()))

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

    int l = 0;
    int r = n - 1;

    int maxi = n;
    int mini = 1;

    bool found = false;

    while (l <= r){

        if (l - r + 1 == 1) break;

        if (nums[l] == mini) {
            l++;
            mini++;
        } else if (nums[l] == maxi) {
            l++;
            maxi--;
        } else if (nums[r] == mini) {
            r--;
            mini++;
        } else if (nums[r] == maxi) {
            r--;
            maxi--;
        } else {
            found = true;
            break;
        }

    }

    if (!found) {
        cout << -1 << "\n";
    } else {
        cout << l + 1 << " " << r + 1 << "\n";
    }

}