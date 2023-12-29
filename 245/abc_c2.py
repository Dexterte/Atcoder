n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(2)]
dp = [[False, False] for _ in range(n)]
dp[0][0] = dp[0][1] = True

for i in range(1, n):
    for j in range(2):
        for k in range(2):
            if dp[i - 1][j]:
                if abs(A[j][i - 1] - A[k][i]) <= m:
                    dp[i][k] = True

if dp[n - 1][0] or dp[n - 1][1]:
    print('Yes')
else:
    print('No')
