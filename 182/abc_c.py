s = input()
n = len(s)
c = [0 for _ in range(3)]
for i in s:
    c[int(i) % 3] += 1

total = 0
for i in range(3):
    total += i * c[i]

INF = 10 ** 9
ans = INF
for i in range(3):
    for j in range(3):
        if c[1] < i: continue
        if c[2] < j: continue
        if i + j == n: continue
        tmp = total
        tmp -= i * 1
        tmp -= j * 2
        if tmp % 3 == 0:
            ans = min(ans, i + j)
if ans == INF:
    ans = -1
print(ans)
