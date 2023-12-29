n, k, x = map(int, input().split())
a = list(map(int, input().split()))

t = 0
b = []
for i in range(n):
    t += a[i] // x
    b.append(a[i] % x)

if k <= t:
    print(sum(a) - k * x)
else:
    b.sort(reverse=True)
    for i in range(min(k - t, n)):
        b[i] = 0
    print(sum(b))
