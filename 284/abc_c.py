n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)

visited = [False for _ in range(n)]


def dfs(v: int):
    """
    深さ優先探索
    :param v: 探索する点
    :return:
    """
    visited[v] = True
    for vi in graph[v]:
        if visited[vi]:
            continue
        dfs(vi)


ans = 0
for i in range(n):
    if visited[i]:
        continue
    dfs(i)
    ans += 1
print(ans)
