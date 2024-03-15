from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))

d = defaultdict(int)
for ai in a:
    d[ai] += 1

ans = 0
for v in d.values():
    ans += v // 2
print(ans)
