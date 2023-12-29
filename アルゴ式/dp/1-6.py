n, m = map(int, input().split())
D = list(map(int, input().split()))

dp = [False for _ in range(n + 1)]
dp[0] = True

for i in range(1, n + 1):
    for j in range(m):
        if i - D[j] >= 0 and dp[i - D[j]]:
            dp[i] = True
print('Yes') if dp[n] else print('No')
