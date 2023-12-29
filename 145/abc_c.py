import itertools
from math import factorial, sqrt

n = int(input())
X = []
Y = []
for i in range(n):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)


num = [i for i in range(n)]

ans = 0

"""_summary_
n!文のパターンを全列挙する
外側のループでN!文のパターンを列挙
"""

for i in itertools.permutations(num):
    dis = 0
    for j in range(n-1):

        index_ = i[j]
        next_index = i[j+1]

        # 距離
        dis += sqrt((X[index_]-X[next_index])**2 +
                    (Y[index_]-Y[next_index])**2)
    ans += dis
print(ans/factorial(n))
