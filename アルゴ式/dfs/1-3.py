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

ans = []


def dfs(v: int):
    visited[v] = True
    ans.append(v)
    for vi in G[v]:
        if visited[vi]:
            continue
        dfs(vi)
    return


dfs(0)
print(*ans)
