n, k = map(int, input().split())
f = []
for i in range(n):
    a, b = map(int, input().split())
    f.append([a, b])

f.sort()

j = 0
# 友達に会わなくてもk番目の村までは辿り着くことができるので、初期位置がk
now = k
while j < n and f[j][0] <= now:
    now += f[j][1]
    j += 1
print(now)
