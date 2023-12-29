import queue

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
deg = [0 for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    deg[b] += 1

queue_ = queue.Queue()

num = 0
for v in range(n):
    if deg[v] == 0:
        queue_.put(v)
        num += 1

while not queue_.empty():
    v = queue_.get()
    for iv in graph[v]:
        deg[iv] -= 1
        if deg[iv] == 0:
            queue_.put(iv)
            num += 1
print('Yes' if num == n else 'No')
