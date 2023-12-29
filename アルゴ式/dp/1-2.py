n = int(input())
A = list(map(int, input().split()))
dp = [0 for _ in range(n)]

dp[1] = A[1]

for i in range(2, n):
    dp[i] = min(2 * A[i] + dp[i - 2], A[i] + dp[i - 1])

print(dp[n - 1])
