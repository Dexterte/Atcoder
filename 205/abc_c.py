a, b, c = map(int, input().split())


def calc(a: int, b: int):
    if b < a:
        print('>')
    elif a < b:
        print('<')
    else:
        print('=')


if c % 2 != 0:
    calc(a, b)
elif c % 2 == 0:
    calc(abs(a), abs(b))
