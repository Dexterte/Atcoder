import itertools

n = list(input())

ans = 0
for v in itertools.permutations(n):
    for i in range(len(n) - 1):
        tmp = int("".join(v[:i + 1])) * int("".join(v[i + 1:]))
        ans = max(tmp, ans)
print(ans)
