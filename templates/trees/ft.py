class BIT:

    def __init__(self, nums):

        self.n = len(nums)
        self.bit = [0] * (self.n + 1)

        for idx, val in enumerate(nums, 1):
            self.update(idx, val)

    def update(self, idx, val):

        while idx <= self.n:
            self.bit[idx] += val
            idx += idx & (-idx)

    def query(self, idx):

        res = 0
        while idx > 0:
            res += self.bit[idx]
            idx -= idx & (-idx)

        return res
    
    def rangeQuery(self, left, right):

        return self.query(right) - self.query(left - 1)