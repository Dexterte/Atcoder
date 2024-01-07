h, w = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(h)]

column_total = [0 for _ in range(w)]
row_total = [0 for _ in range(h)]

for i in range(h):
    row_total[i] = sum(grid[i])

for i in range(w):
    tmp = 0
    for j in range(h):
        tmp += grid[j][i]
    column_total[i] = tmp

for i in range(h):
    ans = []
    for j in range(w):
        ans.append(column_total[j] + row_total[i] - grid[i][j])
    print(*ans)
