import itertools
n, m = map(int, input().split())

friend = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(m):
    x, y = map(int, input().split())
    friend[x][y] = 1
    friend[y][x] = 1

ans = 0
for bit in range(1 << n):
    # 派閥のリスト
    groups = []
    for i in range(n):
        if bit & (1 << i):
            groups.append(i+1)
    # 派閥の人がお互いに知り合いか判定するフラグ
    flag = 1
    for j in itertools.combinations(groups, 2):
        if friend[j[0]][j[1]] == 0:
            flag = 0
            break
    if flag:
        ans = max(ans, len(groups))
print(ans)
