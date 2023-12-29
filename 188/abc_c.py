from collections import deque

n = int(input())
a = list(map(int, input().split()))

b = []
for i, j in enumerate(a):
    b.append((i + 1, j))
b = deque(b)

while 2 < len(b):
    if b[0][1] < b[1][1]:
        b.popleft()
        b.append(b.popleft())
    elif b[1][1] < b[0][1]:
        b.append(b.popleft())
        b.popleft()
b = sorted(b, key=lambda x: x[1])
print(b[0][0])
