from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

dict_ = defaultdict(int)
for i in range(n):
    tmp = b[c[i] - 1]
    dict_[tmp] += 1

ans = 0
for i in range(n):
    ans += dict_[a[i]]
print(ans)
