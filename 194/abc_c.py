from itertools import combinations

n = int(input())
a = list(map(int, input().split()))

MAX_A = 200
ans = 0
d = [0 for _ in range(MAX_A * 2 + 1)]

for i in range(n):
    for j in range(-1 * MAX_A, MAX_A + 1):
        c = d[MAX_A + j]
        x = a[i] - j
        ans += x * x * c
    d[MAX_A + a[i]] += 1
print(ans)
