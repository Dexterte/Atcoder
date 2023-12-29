n = int(input())
P = []
for i in range(n):
    s, t = input().split()
    P.append((s, int(t)))

appeared = set()
# スコア,i番目
original = []
for i in range(n):
    if P[i][0] not in appeared:
        appeared.add(P[i][0])
        original.append((P[i][1], i + 1))
original = sorted(original, key=lambda x: x[0], reverse=True)
print(original[0][1])
