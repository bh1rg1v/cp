class SegmentTreeLP:
    def __init__(self, arr):

        self.n = len(arr)
        self.arr = arr

        self.tree = [0] * (4 * self.n)
        self.lazy = [0] * (4 * self.n)

        self.build(1, 0, self.n - 1)

    def build(self, idx, l, r):

        if l == r:
            self.tree[idx] = self.arr[l]
            return
        
        mid = (l + r) // 2

        self.build(2 * idx, l, mid)
        self.build(2 * idx + 1, mid + 1, r)

        self.tree[idx] = self.tree[2 * idx] + self.tree[2 * idx + 1]

    def push(self, idx, l, r):
        
        if self.lazy[idx] != 0:

            self.tree[idx] += self.lazy[idx] * (r - l + 1)

            if l != r:

                self.lazy[2 * idx] += self.lazy[idx]
                self.lazy[2 * idx + 1] += self.lazy[idx]

            self.lazy[idx] = 0

    def update(self, idx, l, r, ql, qr, val):

        self.push(idx, l, r)

        if ql > r or qr < l:
            return
        if ql <= l and r <= qr:
            self.lazy[idx] += val
            self.push(idx, l, r)
            return
        
        mid = (l + r) // 2

        self.update(2 * idx, l, mid, ql, qr, val)
        self.update(2 * idx + 1, mid + 1, r, ql, qr, val)
        self.push(2 * idx, l, mid)
        self.push(2 * idx + 1, mid + 1, r)

        self.tree[idx] = self.tree[2 * idx] + self.tree[2 * idx + 1]

    def query(self, idx, l, r, ql, qr):

        if ql > r or qr < l:
            return 0
        
        self.push(idx, l, r)
        if ql <= l and r <= qr:
            return self.tree[idx]
        
        mid = (l + r) // 2
        left = self.query(2 * idx, l, mid, ql, qr)
        right = self.query(2 * idx + 1, mid + 1, r, ql, qr)
        
        return left + right