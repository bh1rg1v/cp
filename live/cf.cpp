#include <bits/stdc++.h>
using namespace std;

struct Node {
    long long val;
    int idx;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;

        vector<long long> a(n), b(n), c(n);
        for (int i = 0; i < n; i++) cin >> a[i];
        for (int i = 0; i < n; i++) cin >> b[i];
        for (int i = 0; i < n; i++) cin >> c[i];

        auto topk = [&](vector<long long> &arr) {
            vector<Node> res;
            for (int i = 0; i < n; i++) {
                res.push_back({arr[i], i});
            }
            sort(res.begin(), res.end(), [](auto &x, auto &y) {
                return x.val > y.val;
            });
            if (res.size() > 5) res.resize(5);  // keep top 5
            return res;
        };

        vector<Node> A = topk(a);
        vector<Node> B = topk(b);
        vector<Node> C = topk(c);

        long long ans = 0;
        for (auto &x : A) {
            for (auto &y : B) {
                for (auto &z : C) {
                    if (x.idx != y.idx && y.idx != z.idx && x.idx != z.idx) {
                        ans = max(ans, x.val + y.val + z.val);
                    }
                }
            }
        }

        cout << ans << "\n";
    }
    return 0;
}