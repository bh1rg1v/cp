from collections import Counter
from functools import reduce
from math import *
import heapq
from collections import deque

for _ in range(int(input())):

    n = int(input())
    edges = []

    for i in range(n-1):
        edges.append(list(map(int, input().split())))            