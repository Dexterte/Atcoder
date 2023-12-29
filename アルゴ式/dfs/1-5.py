n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False for _ in range(n)]
visited[0] = True


def dfs(v: int):
    visited[v] = True
    for vi in graph[v]:
        if visited[vi]:
            continue
        dfs(vi)
    return


dfs(0)
for i in range(n):
    if not visited[i]:
        print('No')
        exit()
print('Yes')
