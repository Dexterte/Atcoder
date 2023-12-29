n,m=map(int,input().split())
A=[list(map(int,input().split())) for _ in range(n)]
ans = 0
for i in range(m):
    for j in range(i,m):
        cnt = 0
        for k in range(n):
            cnt+=max(A[k][i],A[k][j])
        ans=max(ans,cnt)
print(ans)

# highScore = []
# #tmpに入る個数
# cnt = 0
# for i in range(n):
#     tmp = []
#     for j in range(m-1):
#         for k in range(j+1,m):
#             tmp.append(max(A[i][j],A[i][k]))
#             cnt+=1
#     highScore.append(tmp)
# cnt = cnt//n
# ans = []
# for i in range(cnt):
#     score = 0
#     for j in range(n):
#         score+=highScore[j][i]
#     ans.append(score)
# print(max(ans))
