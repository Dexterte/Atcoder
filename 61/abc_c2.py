# 別解

S = list(map(int,input()))
n = len(S)

ans = 0
for bit in range(1 << n-1):
    tmp = 0
    for i in range(n-1):
        tmp *= 10
        tmp += S[i]
        if (bit & (1 << i)):
            ans += tmp
            tmp = 0
    tmp *= 10
    tmp += S[n-1]
    ans += tmp
print(ans)
