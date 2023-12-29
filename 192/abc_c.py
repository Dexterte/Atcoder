import copy

n, k = map(int, input().split())


def calc(s: int) -> int:
    tmp = [i for i in str(s)]
    tmp.sort()
    g1 = copy.deepcopy(tmp)
    tmp.reverse()
    g2 = copy.deepcopy(tmp)
    diff = int("".join(g2)) - int("".join(g1))
    return diff


for i in range(k):
    n = calc(n)
print(n)
