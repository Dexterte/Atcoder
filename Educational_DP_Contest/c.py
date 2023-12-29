n = int(input())
happiness = []
for i in range(n):
    a, b, c = map(int, input().split())
    happiness.append([a, b, c])

dp = [[0, 0, 0] for _ in range(n)]
dp[0][0] = happiness[0][0]
dp[0][1] = happiness[0][1]
dp[0][2] = happiness[0][2]

for i in range(1, n):
    dp[i][0] = max(dp[i - 1][1] + happiness[i][0], dp[i - 1][2] + happiness[i][0])
    dp[i][1] = max(dp[i - 1][0] + happiness[i][1], dp[i - 1][2] + happiness[i][1])
    dp[i][2] = max(dp[i - 1][0] + happiness[i][2], dp[i - 1][1] + happiness[i][2])

print(max(dp[n - 1]))
