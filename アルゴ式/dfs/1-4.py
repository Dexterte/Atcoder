n, m = map(int, input().split())
graph = []
for i in range(m):
    a, b = map(int, input().split())
    graph.append((a, b))
visited = [False for _ in range(n)]
visited[0] = True

G = [[] for _ in range(n)]
for i in range(m):
    G[graph[i][0]].append(graph[i][1])

for i in range(n):
    G[i].sort()


def dfs(v: int):
    visited[v] = True
    for vi in G[v]:
        if visited[vi]:
            continue
        dfs(vi)


dfs(0)
ans = 0
for i in range(n):
    if not visited[i]:
        ans += 1
print(ans)
