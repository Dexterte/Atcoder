n, m = map(int, input().split())
h = list(map(int, input().split()))
status = [True for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if h[a] <= h[b]:
        status[a] = False
    if h[b] <= h[a]:
        status[b] = False
print(status.count(True))
