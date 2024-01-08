from bisect import bisect_left

n = int(input())
a = list(map(int, input().split()))
q = int(input())
b = [int(input()) for _ in range(q)]

a.sort()

for i in range(q):
    index = bisect_left(a, b[i])
    if index <= 0:
        ans = abs(b[i] - a[index])
    elif n <= index:
        ans = abs(b[i] - a[index - 1])
    else:
        ans = min(abs(b[i] - a[index]), abs(b[i] - a[index - 1]))
    print(ans)
