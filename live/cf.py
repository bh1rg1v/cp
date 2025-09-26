import sys
from collections import Counter, defaultdict, deque, namedtuple
import heapq, bisect, string
from math import gcd, lcm, sqrt, ceil, floor, factorial, comb, perm, log2
from itertools import permutations, combinations, product, accumulate, groupby
from functools import lru_cache, reduce


for t in range(int(input())):

    # n, k = map(int, input().split())
    n = int(input())
    
    arr = list(map(str, input().split()))

    a = arr.count('a')
    b = arr.count('b')

    
    