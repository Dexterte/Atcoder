n, x, y = map(int, input().split())
dp = [0 for _ in range(102)]

dp[0] = x
dp[1] = y
for i in range(2, n):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 100
print(dp[n - 1])
