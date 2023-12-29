import queue

h, w = map(int, input().split())
X = list(map(int, input().split()))
game_board = [input() for _ in range(h)]

start_x, start_y = X[0], X[1]
goal_x, goal_y = X[2], X[3]
dist = [[-1 for _ in range(w)] for _ in range(h)]
queue_ = queue.Queue()

dist[start_x][start_y] = 0
queue_.put((start_x, start_y))

while not queue_.empty():
    x, y = queue_.get()
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    for i in range(4):
        next_x = dx[i] + x
        next_y = dy[i] + y
        if next_x < 0 or h <= next_x or next_y < 0 or w <= next_y:
            continue
        if game_board[next_x][next_y] == 'B':
            continue
        if dist[next_x][next_y] != -1:
            continue
        dist[next_x][next_y] = dist[x][y] + 1
        queue_.put((next_x, next_y))

print(dist[goal_x][goal_y])
