from itertools import product

n = int(input())


def is_valid(s: str) -> bool:
    score = 0
    for c in s:
        if c == '(':
            score += 1
        else:
            score -= 1
        if score < 0:
            return False
    return score == 0


for s in product(['(', ')'], repeat=n):
    if is_valid(s):
        print(*s, sep='')
