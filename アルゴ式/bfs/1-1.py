import queue

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 各頂点の深さを管理する
dist = [-1 for _ in range(n)]
que = queue.Queue()

# 頂点0を初期ノードとする
dist[0] = 0
que.put(0)

while not que.empty():
    v = que.get()
    for iv in graph[v]:
        # 既に発見済みの頂点は探索しない
        if dist[iv] != -1:
            continue
        # 新たな白色頂点ivについて距離情報を更新して、キューに追加する
        dist[iv] = dist[v] + 1
        que.put(iv)

ans = [[] for _ in range(n)]
for i in range(n):
    tmp = dist[i]
    if -1 < tmp:
        ans[tmp].append(i)

for i in ans:
    print(*i)
