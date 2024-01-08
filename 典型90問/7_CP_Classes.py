from bisect import bisect_left

n = int(input())
a = list(map(int, input().split()))
q = int(input())
b = [int(input()) for _ in range(q)]

a.sort()

for i in range(q):
    index = bisect_left(a, b[i])
    result = float('inf')
    if index < n:
        result = min(result, abs(b[i] - a[index]))
    if index > 0:
        result = min(result, abs(b[i] - a[index - 1]))
    print(result)
