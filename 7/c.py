import queue

r, c = map(int, input().split())
start_y, start_x = map(int, input().split())
start_y, start_x = start_y - 1, start_x - 1
goal_y, goal_x = map(int, input().split())
goal_y, goal_x = goal_y - 1, goal_x - 1
board = []
for i in range(r):
    a = list(input())
    board.append(a)

dist = [[-1 for _ in range(c)] for _ in range(r)]
queue_ = queue.Queue()

dist[start_y][start_y] = 0
queue_.put((start_y, start_x))

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
while not queue_.empty():
    y, x = queue_.get()
    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]
        if next_y < 0 or r <= next_y or next_x < 0 or c <= next_x:
            continue
        if board[next_y][next_x] == '#':
            continue
        if dist[next_y][next_x] != -1:
            continue
        dist[next_y][next_x] = dist[y][x] + 1
        queue_.put((next_y, next_x))
print(dist[goal_y][goal_x])
