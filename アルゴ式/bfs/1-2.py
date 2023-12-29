import queue

n, m = map(int, input().split())
friends = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

dist = [-1 for _ in range(n)]
que = queue.Queue()

dist[0] = 0
que.put(0)

while not que.empty():
    v = que.get()
    for vi in friends[v]:
        if dist[vi] != -1:
            continue
        dist[vi] = dist[v] + 1
        que.put(vi)
print(max(dist))
