#include <bits/stdc++.h>
using namespace std;

void solve() {

    int n;
    cin >> n;

    int s = (n * (n - 1)) / 2;
    vector<int> nums(s, 0);

    for (int i = 0; i < s; i++){
        cin >> nums[i];
    }

    sort(nums.begin(), nums.end());

    int j = 0;

    for (int i = n - 1; i > 0; i--){
        cout << nums[j] << " ";
        j += i;
    }

    cout << int(1e9) << endl;



}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--) solve();

    return 0;
}