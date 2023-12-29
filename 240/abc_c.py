from operator import truediv


n,x=map(int,input().split())
A = []
B = []
for i in range(n):
    a,b=map(int,input().split())
    A.append(a)
    B.append(b)
dp = [[False for _ in range(x+1)] for _ in range(n+1)]
dp[0][0]=True
for i in range(n):
    for j in range(x+1):
        if(dp[i][j]):
            #枠をはみ出していないか？
            if(j+A[i] <= x):
                dp[i+1][j+A[i]]=True
            #枠をはみ出していないか？
            if(j+B[i] <= x):
                dp[i+1][j+B[i]]=True
print("Yes") if dp[n][x] else print("No")
