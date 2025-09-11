from collections import Counter
from functools import reduce
from math import *

for _ in range(int(input())):

    n = int(input())

    org = n
    cnt1 = 0
    while n % 25 != 0:

        while str(n)[-1] != '5':
            n = int((str(n))[:-1])
            cnt1 += 1

        while str(n)[-2] not in "27":
            n = int(str(n)[:-2] + str(n)[-1])
            cnt1 += 1

    n = org
    cnt2 = 0
    while n % 25 != 0:

        while str(n)[-1] != '0' and len(str(n)) > 2:
            print(f"1. {n=}")
            n = int((str(n))[:-1])
            cnt2 += 1

        while len(str(n)) > 2 and str(n)[-2] not in "05":
            n = int(str(n)[:-2] + str(n)[-1])
            cnt2 += 1
    
    cnt = min(cnt1, cnt2)
    print(f"{cnt=}")