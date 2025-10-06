#include <bits/stdc++.h>
using namespace std;

void solve() {

    long long n, x, y;
    cin >> n >> x >> y;

    if (x == y) {
        cout << 0 << endl;
        return;
    }

    // if (x < y) swap(x, y);

    long long lcm = x / gcd(x, y) * y;

    long long pos = (n / x) - (n / lcm);
    long long neg = (n / y) - (n / lcm);

    long long a = n - pos;

    pos = ((n * (n + 1)) / 2) - ((a * (a + 1)) / 2);
    neg = (neg * (neg + 1)) / 2;

    long long ans = pos - neg;

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