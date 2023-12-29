n = int(input())
a = [int(input()) for _ in range(n)]
counter = [0 for _ in range(n)]

for i in range(n):
    counter[a[i] - 1] += 1

x = -1
y = -1
for i in range(n):
    if counter[i] <= 0 or 2 <= counter[i]:
        if 2 <= counter[i]:
            x = i + 1
        elif counter[i] <= 0:
            y = i + 1
if x == -1 and y == -1:
    print('Correct')
else:
    print(x, y)
