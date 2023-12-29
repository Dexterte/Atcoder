n = int(input())
s = list(input())
ans = 0
for i in range(10):
    for j in range(10):
        for k in range(10):
            num=(i,j,k)
            cnt = 0
            for l in range(n):
                if num[cnt]== int(s[l]):
                    cnt+=1
                if cnt == 3:
                    ans+=1
                    break
print(ans)
