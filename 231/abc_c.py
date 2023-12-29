from bisect import bisect_left

n, q = map(int, input().split())
a = list(map(int, input().split()))
x = [int(input()) for _ in range(q)]

a.sort()

for x in x:
    result = bisect_left(a, x)
    print(n - result)
