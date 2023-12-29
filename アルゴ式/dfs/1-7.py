h, w = map(int, input().split())
S = [input() for _ in range(h)]
visited = [[False for _ in range(w)] for _ in range(h)]


def dfs(y: int, x: int):
    visited[y][x] = True
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]
        if next_x < 0 or w <= next_x or next_y < 0 or h <= next_y:
            continue
        elif visited[next_y][next_x]:
            continue
        elif S[next_y][next_x] == '.':
            continue
        dfs(next_y, next_x)
    return


ans = 0
for i in range(h):
    for j in range(w):
        if visited[i][j] or S[i][j] == '.':
            continue
        dfs(i, j)
        ans += 1
print(ans)
