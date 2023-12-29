n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    a[i] = a[i] - 1

ans = 0
cnt = 0
for i in range(n):
    if a[i] == i:
        cnt += 1
ans = cnt * (cnt - 1) // 2

for i in range(n):
    if a[i] <= i:
        continue
    if a[a[i]] == i:
        ans += 1
print(ans)
