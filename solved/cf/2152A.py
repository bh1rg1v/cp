import sys
from collections import Counter, defaultdict, deque, namedtuple
import heapq, bisect, string
from math import gcd, lcm, sqrt, ceil, floor, factorial, comb, perm, log2
from itertools import permutations, combinations, product, accumulate, groupby
from functools import lru_cache, reduce


for t in range(int(input())):

    n = int(input())
    nums = list(map(int, input().split()))

    # n, k = map(int, input().split())
    # nums = list(map(int, input().split()))

    # n, m = map(int, input().split())
    # mat = [list(map(int, input().split())) for _ in range(n)]

    
    # if n == 1:
    #     print(1)
    #     continue

    n = len(set(nums))

    print((n - 1) * 2 + 1)
    