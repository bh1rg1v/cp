#include <bits/stdc++.h>
using namespace std;

vector<int> threeLargest(const vector<long long>& arr) {

    int n = arr.size();
    vector<int> idx(n);

    iota(idx.begin(), idx.end(), 0);
    sort(idx.begin(), idx.end(), [&](int i, int j) {
        return arr[i] > arr[j];
    });

    if (n > 3) idx.resize(3);
    return idx;
}

void solve() {
    int n;
    cin >> n;

    vector<long long> a(n), b(n), c(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    for (int i = 0; i < n; i++) cin >> b[i];
    for (int i = 0; i < n; i++) cin >> c[i];

    vector<int> bestA = threeLargest(a);
    vector<int> bestB = threeLargest(b);
    vector<int> bestC = threeLargest(c);

    long long ans = 0;
    for (int x : bestA) {
        for (int y : bestB) {
            for (int z : bestC) {
                if (x != y && y != z && x != z) {
                    ans = max(ans, a[x] + b[y] + c[z]);
                }
            }
        }
    }
    cout << ans << endl;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--) solve();

    return 0;
}