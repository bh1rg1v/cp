from collections import Counter
from functools import reduce
from math import *
import heapq
from collections import deque

for _ in range(int(input())):

    n = int(input())
    s = input()
    nums = list(map(int, s.strip()))

    a = nums.count(0)
    b = nums.count(1)

    if n == a or n == b:
        print("YES")
        continue

    print(nums)
    flag = False
    idx = 0
    prevsOnesCnt = 0

    idxes = deque([idx for idx in range(n) if nums[idx] == 0])

    while idxes:

        idx = idxes.popleft()

        prevOnes = 0
        nextOnes = 0

        if idx == 0:
            prevOnes = 0
        else:
            temp = idx - 1
            while temp > -1 and nums[temp] == 1:
                prevOnes += 1
                temp -= 1

        if idx == n - 1:
            nextOnes = 0
        else:
            temp = idx + 1
            while temp < n and nums[temp] == 1:
                nextOnes += 1
                temp += 1

        if prevOnes >= 2 and nextOnes >= 2:
            flag = True
            break

        


    print("NO" if flag else "YES")
        

        