n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

a_now = 0
b_now = 0
ans = float('inf')
while a_now < n and b_now < m:
    diff = abs(a[a_now] - b[b_now])
    ans = min(diff, ans)
    if a[a_now] <= b[b_now]:
        a_now += 1
    else:
        b_now += 1
print(ans)
