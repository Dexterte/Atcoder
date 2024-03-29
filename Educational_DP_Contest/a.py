n = int(input())
h = list(map(int, input().split()))

dp = [float('inf') for _ in range(n)]
dp[0] = 0
dp[1] = abs(h[0] - h[1])

for i in range(2, n):
    dp[i] = min(dp[i - 2] + abs(h[i] - h[i - 2]), dp[i - 1] + abs(h[i] - h[i - 1]))
print(dp[n - 1])
