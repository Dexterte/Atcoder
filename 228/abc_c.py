n, k = map(int, input().split())
score = []
for i in range(n):
    p = list(map(int, input().split()))
    score.append((sum(p)))

sorted_score = sorted(score, reverse=True)

for i in range(n):
    if score[i] + 300 >= sorted_score[k - 1]:
        print('Yes')
    else:
        print('No')
