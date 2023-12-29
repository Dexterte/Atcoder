a,b,c,x,y=map(int,input().split())
ans = []
for k in range(10**6):
    #kはabピザを買う枚数
    tmp = 2*c*k + max(x-k,0)*a+max(y-k,0)*b
    ans.append(tmp)
print(min(ans))
