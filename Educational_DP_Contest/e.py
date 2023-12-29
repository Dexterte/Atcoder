N, W = map(int, input().split())
weight = []
value = []
for i in range(N):
    w, j = map(int, input().split())
    weight.append(w)
    value.append(j)

dp = [[float('inf') for _ in range(10 ** 5 + 1)] for _ in range(N + 1)]
dp[0][0] = 0

for i in range(N):
    for j in range(10 ** 5 + 1):
        dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
        if j - value[i] >= 0:
            dp[i + 1][j] = min(dp[i + 1][j], dp[i][j - value[i]] + weight[i])

for i in range(10 ** 5, 0, -1):
    if dp[N][i] <= W:
        print(i)
        exit()
