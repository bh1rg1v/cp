#include <bits/stdc++.h>
using namespace std;

void solve() {

    int n;
    cin >> n;

    vector<long long> a(n);
    for (int i = 0; i < n; i++) { 
        cin >> a[i];
    }

    long long ans = 2;
    bool found = false;

    while (true) {
        
        set<long long> mods;
        for (int i = 0; i < n; i++) {
            mods.insert(a[i] % ans);
        }

        if (mods.size() == 2) {
            found = true;
            break;
        }
        ans *= 2;
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