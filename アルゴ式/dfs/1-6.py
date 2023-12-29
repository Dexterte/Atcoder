n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False for _ in range(n)]


def dfs(v: int):
    visited[v] = True
    for vi in graph[v]:
        if visited[vi]:
            continue
        dfs(vi)
    return


ans = 0
for v in range(n):
    if visited[v]:
        continue
    dfs(v)
    ans += 1
print(ans)
