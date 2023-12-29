n = int(input())
T = []
for _ in range(n):
    t, l, r = map(int, input().split())
    if t % 2 == 0:
        r -= 0.5
    if t >= 3:
        l += 0.5
    T.append((t, l, r))

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        if max(T[i][1], T[j][1]) <= min(T[i][2], T[j][2]):
            ans += 1
print(ans)
