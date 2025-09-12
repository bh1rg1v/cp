class FT:

    def __init__(self, nums):

        self.n = len(nums)
        self.FT = [0] * (self.n + 1)

        for i in range(self.n):
            self.update(i + 1, nums[i])

    def update(self, i, val):

        while i <= self.n:
            self.FT[i] += val
            i += i & (-i)

    def getSum(self, i):

        res = 0
        while i > 0:
            res += self.FT[i]
            i -= i & (-i)

        return res