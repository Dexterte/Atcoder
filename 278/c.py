n, q = map(int, input().split())
T = []
for i in range(q):
    t, a, b = map(int, input().split())
    T.append((t, a, b))

follow = set()


def is_mutual_follow(a: int, b: int):
    return (a, b) in follow and (b, a) in follow


for i in range(q):
    a = T[i][1] - 1
    b = T[i][2] - 1
    if T[i][0] == 1:
        follow.add((a, b))
    elif T[i][0] == 2:
        if (a, b) in follow:
            follow.remove((a, b))
    elif T[i][0] == 3:
        if is_mutual_follow(a, b):
            print('Yes')
        else:
            print('No')
