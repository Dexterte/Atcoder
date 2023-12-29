n, w = map(int, input().split())
W = []
V = []
for i in range(n):
    a, b = map(int, input().split())
    W.append(a)
    V.append(b)
W.insert(0, 0)
V.insert(0, 0)

dp = [[0 for _ in range(w + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(w + 1):
        dp[i][j] = dp[i - 1][j]
        if j - W[i] >= 0:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - W[i]] + V[i])
print(dp[n][w])
