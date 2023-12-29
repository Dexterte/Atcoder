from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))

dict_ = defaultdict(int)

ans = 0
for i in range(n):
    ans += i - dict_[a[i]]
    dict_[a[i]] += 1
print(ans)
