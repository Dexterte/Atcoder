from collections import defaultdict

n = int(input())
S = [input() for _ in range(n)]

duplication = defaultdict(int)

for s in S:
    if duplication[s] == 0:
        print(s)
    else:
        print("{0}({1})".format(s, duplication[s]))
    duplication[s] += 1
