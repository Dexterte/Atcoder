n, w = map(int, input().split())
W = []
V = []
for i in range(n):
    a, b = map(int, input().split())
    W.append(a)
    V.append(b)

dp = [[0 for _ in range(w + 1)] for _ in range(n + 1)]

for i in range(n):
    for j in range(w + 1):
        dp[i + 1][j] = dp[i][j]
        if j - W[i] >= 0:
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j - W[i]] + V[i])
        else:
            dp[i + 1][j] = dp[i][j]
print(dp[n][w])
