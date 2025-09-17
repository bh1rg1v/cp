class SegmentTree:
    def __init__(self, arr, mode="min"):

        self.n = len(arr)
        self.arr = arr
        self.mode = mode
        self.tree = [0] * (4 * self.n + 1)
        self.build(1, 0, self.n - 1)

    def combine(self, left, right):
        return min(left, right) if self.mode == "min" else max(left, right)

    def build(self, idx, l, r):

        if l == r:
            self.tree[idx] = self.arr[l]
            return
        
        mid = (l + r) // 2
        self.build(2 * idx, l, mid)
        self.build(2 * idx + 1, mid + 1, r)
        self.tree[idx] = self.combine(self.tree[2 * idx], self.tree[2 * idx + 1])

    def update(self, idx, l, r, pos, val):

        if l == r:
            self.tree[idx] = val
            return
        
        mid = (l + r) // 2
        if pos <= mid:
            self.update(2 * idx, l, mid, pos, val)
        else:
            self.update(2 * idx + 1, mid + 1, r, pos, val)
        
        self.tree[idx] = self.combine(self.tree[2 * idx], self.tree[2 * idx + 1])

    def query(self, idx, l, r, ql, qr):

        if ql > r or qr < l:
            return float("inf") if self.mode == "min" else float("-inf")
        
        if ql <= l and r <= qr:
            return self.tree[idx]
        
        mid = (l + r) // 2
        left = self.query(2 * idx, l, mid, ql, qr)
        right = self.query(2 * idx + 1, mid + 1, r, ql, qr)
        return self.combine(left, right)