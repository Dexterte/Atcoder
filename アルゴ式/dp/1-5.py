n, m = map(int, input().split())
A = list(map(int, input().split()))

dp = [0 for _ in range(n)]
dp[1] = A[1]

for i in range(2, n):
    tmp = []
    for j in range(1, m + 1):
        if i - j >= 0:
            tmp.append(j * A[i] + dp[i - j])
    dp[i] = min(tmp)
print(dp[n - 1])
