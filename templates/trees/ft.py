class FT:

    def __init__(self, nums):

        self.n = len(nums)
        self.FT = [0] * (self.n + 1)

        for idx in range(self.n):
            self.update(idx + 1, nums[idx])

    def update(self, idx, val):

        while idx <= self.n:
            self.FT[idx] += val
            idx += idx & (-idx)

    def getSum(self, idx):

        res = 0
        while idx > 0:
            res += self.FT[idx]
            idx -= idx & (-idx)

        return res