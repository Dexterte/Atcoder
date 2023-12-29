n = int(input())
t = [int(input()) for _ in range(n)]

ans = []
for bit in range(1 << n):
    # 一つ目の肉焼き器
    x = 0
    # 二つ目の肉焼き器
    y = 0
    for i in range(n):
        if bit & (1 << i):
            x += t[i]
        else:
            y += t[i]
    ans.append(max(x, y))
print(min(ans))
