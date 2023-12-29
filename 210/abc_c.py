from collections import defaultdict

n, k = map(int, input().split())
c = list(map(int, input().split()))

ans = 0
kind_number = 0
dict_ = defaultdict(int)

for i in range(n):
    if i - k >= 0:
        if dict_[c[i - k]] == 1:
            kind_number -= 1
        dict_[c[i - k]] -= 1

    if dict_[c[i]] == 0:
        kind_number += 1
    dict_[c[i]] += 1
    ans = max(ans, kind_number)
print(ans)
