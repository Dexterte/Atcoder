n, k = map(int, input().split())
a = list(map(int, input().split()))

b = []
for i in range(n):
    b.append((i, a[i]))
b = sorted(b, key=lambda x: x[1])

ans = [k // n for _ in range(n)]

extra_amount = k % n
for i in range(extra_amount):
    ans[b[i][0]] += 1

for i in ans:
    print(i)