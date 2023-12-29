from itertools import permutations

n = int(input())
P = list(input().split())
Q = list(input().split())

N = [str(i+1) for i in range(n)]


# 順列が何番目かを数える
cnt = 0

"""_summary_
全列挙して、a番目とb番目を数える
"""

for i in permutations(N):

    cnt += 1

    if P == list(i):
        # a番目
        p_cnt = cnt
    if Q == list(i):
        # b番目
        q_cnt = cnt

print(abs(p_cnt-q_cnt))
