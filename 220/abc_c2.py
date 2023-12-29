n = int(input())
a = list(map(int, input().split()))
x = int(input())

total = sum(a)
ans = (x // total) * n
tmp = 0
for i in range(n):
    tmp += a[i]
    ans += 1
    if tmp > x % total:
        break
print(ans)
