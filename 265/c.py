h, w = map(int, input().split())
graph = [list(input()) for _ in range(h)]

visited = [[False for _ in range(w)] for _ in range(h)]
now_x, now_y = 0, 0
for _ in range(500 * 500):
    if visited[now_y][now_x]:
        print(-1)
        exit()

    if graph[now_y][now_x] == 'U' and now_y != 0:
        visited[now_y][now_x] = True
        now_y -= 1
    if graph[now_y][now_x] == 'D' and now_y != h - 1:
        visited[now_y][now_x] = True
        now_y += 1
    if graph[now_y][now_x] == 'L' and now_x != 0:
        visited[now_y][now_x] = True
        now_x -= 1
    if graph[now_y][now_x] == 'R' and now_x != w - 1:
        visited[now_y][now_x] = True
        now_x += 1

print(now_y + 1, now_x + 1)
