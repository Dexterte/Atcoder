n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
dp = [[False, False] for _ in range(n)]
dp[0][0] = dp[0][1] = True

for i in range(1, n):
    if dp[i - 1][0]:
        if abs(A[i - 1] - A[i]) <= k:
            dp[i][0] = True
        if abs(A[i - 1] - B[i]) <= k:
            dp[i][1] = True
    if dp[i - 1][1]:
        if abs(B[i - 1] - A[i]) <= k:
            dp[i][0] = True
        if abs(B[i - 1] - B[i]) <= k:
            dp[i][1] = True

if dp[n - 1][0] or dp[n - 1][1]:
    print('Yes')
else:
    print('No')
