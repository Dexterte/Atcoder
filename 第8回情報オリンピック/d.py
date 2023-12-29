n = int(input())
m = int(input())
A = [list(map(int, input().split())) for _ in range(m)]

# 訪問済みか記録
visited = [[False for _ in range(n)] for _ in range(m)]

def dfs(x, y):

    # 訪問済みにする
    visited[x][y] = True

    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    # 頂点vからnext_vに移動する
    for i in range(4):
        next_x = x+dx[i]
        next_y = y+dy[i]
        """
        next_vが探索済み又は枠外または氷の上以外であれば探索しない
        割った数の氷が最大値であるか比較
        """
        if next_x < 0 or next_x <= m or next_y < 0 or next_y <= n or visited[next_x][next_y] or A[next_x][next_y] == 0:
            continue

        # 再帰探索
        dfs(next_x, next_y)


