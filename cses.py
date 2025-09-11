
n = int(input())
nums = list(map(int, input().split()))

nums = set(nums)

for i in range(1, n + 1):
    if i not in nums:
        print(i)
        break