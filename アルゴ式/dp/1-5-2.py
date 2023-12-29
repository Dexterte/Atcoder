n, m = map(int, input().split())
A = list(map(int, input().split()))

dp = [float('inf') for _ in range(n)]
dp[0] = 0

for i in range(1, n):
    for j in range(1, m + 1):
        if i - j >= 0:
            dp[i] = min(dp[i], j * A[i] + dp[i - j])
print(dp[n - 1])
