n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

A = [(ai, i) for i, ai in enumerate(a)]
B = [(bi, i + n) for i, bi in enumerate(b)]

C = A + B
C = sorted(C, key=lambda x: x[0])

order_a = [0 for _ in range(n)]
order_b = [0 for _ in range(m)]
order = 1
for i in range(n + m):
    target_index = C[i][1]
    if target_index < n:
        order_a[target_index] = order
    else:
        order_b[target_index - n] = order
    order += 1

print(*order_a)
print(*order_b)
