n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

rank_a = [0 for _ in range(n)]
rank_b = [0 for _ in range(m)]

ai, bi = 0, 0
rank = 1
while rank_a[n - 1] == 0 or rank_b[m - 1] == 0:
    if n <= ai:
        rank_b[bi] = rank
        bi += 1
        rank += 1
        continue
    elif m <= bi:
        rank_a[ai] = rank
        ai += 1
        rank += 1
        continue
    if a[ai] < b[bi]:
        rank_a[ai] = rank
        ai += 1
    elif b[bi] < a[ai]:
        rank_b[bi] = rank
        bi += 1
    rank += 1

print(*rank_a)
print(*rank_b)
