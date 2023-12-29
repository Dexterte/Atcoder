n = int(input())
A = []
B = []
for i in range(n):
    a,b=map(int,input().split())
    A.append(a)
    B.append(b)

ans = []

for i in range(n):
    for j in range(n):
        dis = 0
        for k in range(n):
            #A[i]:スタート(s)
            #B[j]:ゴール(t)
            dis += abs(A[k]-A[i])+abs(A[k]-B[k])+abs(B[k]-B[j])
        ans.append(dis)
print(min(ans))
