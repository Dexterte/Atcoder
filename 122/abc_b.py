S=input()
# S=S+"0"
n = len(S)
atcg = ["A","C","G","T"]
cnt = 0
ans = [0]
for i in range(n-1):
    if S[i] in atcg:
        cnt+=1
        if S[i+1] in atcg:
            continue
        else:
            ans.append(cnt)
            cnt = 0
print(max(ans))
