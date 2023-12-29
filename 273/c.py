from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))

dict_ = defaultdict(int)

for i in range(n):
    dict_[a[i]] += 1

dict_ = sorted(dict_.items(), key=lambda x: x[0], reverse=True)

result = [dict_[i][1] for i in range(len(dict_))]
while len(result) < n:
    result.append(0)

for i in range(n):
    print(result[i])
