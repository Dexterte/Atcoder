import itertools

n, k = map(int, input().split())
T = []
for i in range(n):
    t = list(map(int, input().split()))
    T.append(t)

ans = 0

permutations = itertools.permutations(list(range(1, n)))
for route in permutations:
    time = 0
    # 1から初めの都市を訪れる
    time += T[0][route[0]]
    for j in range(n - 2):
        time += T[route[j]][route[j + 1]]
    # 最後の都市から1に戻る
    time += T[0][route[n - 2]]
    if time == k:
        ans += 1
print(ans)
