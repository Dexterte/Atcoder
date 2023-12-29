import sys
sys.setrecursionlimit(10**6)

h, w = map(int, input().split())
C = [list(input()) for _ in range(h)]

# 訪問済みか記録する
visited = [[False for _ in range(w)] for _ in range(h)]

"""
深さ優先探索
再帰関数を使うパターン
"""


def dfs(x, y):
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    # 訪問済みにする
    visited[x][y] = True

    # 座標v(x,y)から行ける頂点next_v(next_x,next_y)のループをまわす
    for i in range(4):
        next_x = x+dx[i]
        next_y = y+dy[i]

    # next_x,next_yが探索済みまたは枠外・塀であれば探索しない
        if next_y < 0 or w <= next_y or next_x < 0 or h <= next_x or C[next_x][next_y] == "#" or visited[next_x][next_y]:
            continue

    # 再帰的に探索
        dfs(next_x, next_y)



def main():
    for i in range(h):
        for j in range(w):
            if C[i][j] == "s":
                sx, sy = i, j
            if C[i][j] == "g":
                gx, gy = i, j

    # 探索
    dfs(sx, sy)

    # ゴールの箇所がTrueになっていれば、Yesを出力
    print("Yes") if visited[gx][gy] else print("No")


if __name__ == '__main__':
    main()
