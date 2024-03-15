n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

order_a = [0 for _ in range(n)]
order_b = [0 for _ in range(m)]

ai, bi = 0, 0
order = 1
while order_a[n - 1] == 0 or order_b[m - 1] == 0:
    if n <= ai:
        order_b[bi] = order
        bi += 1
        order += 1
        continue
    elif m <= bi:
        order_a[ai] = order
        ai += 1
        order += 1
        continue
    if a[ai] < b[bi]:
        order_a[ai] = order
        ai += 1
    elif b[bi] < a[ai]:
        order_b[bi] = order
        bi += 1
    order += 1

print(*order_a)
print(*order_b)
