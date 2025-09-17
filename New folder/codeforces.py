from collections import Counter
from functools import reduce
from math import *

for _ in range(int(input())):

    n = int(input())
    nums = list(map(int, input().split()))

    ans = 0

    numsSet = set(nums)

    absent = []
    for num in range(1, n+1):
        if num not in numsSet:
            absent.append(num)

    indexes = []
    for i, num in enumerate(nums):
        if num == 0:
            indexes.append(i)

    def findSeg(nums):
        start = float('inf')
        end = float('-inf')

        for i, num in enumerate(nums, 1):
            if i != num:
                start = min(start, i)
                end = max(end, i)

        return start, end

    if indexes:
        maxIdx = max(indexes)
        minIdx = min(indexes)
    else:

        if nums == sorted(nums):
            print(0)
            continue
        
        start, end = findSeg(nums)
        ans = end - start + 1
        print(ans)
        continue

    if minIdx == maxIdx:

        ans = 0
        missing = ((n * (n+1)) // 2) - sum(nums)
        nums[minIdx] = missing

        if nums == sorted(nums):
            ans = 0
        else:

            start, end = findSeg(nums)

            # print(f"{start=}, {end=}")
            ans = end - start + 1
            # print(f"{ans=}")

        # print(f"{nums=}")
    else:
        ans = maxIdx - minIdx + 1

    # print(f"{ans=}")
    print(ans)
