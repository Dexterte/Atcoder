import math

_n = int(input())


def make_divisor(n: int) -> list[int]:
    """
    約数を列挙する
    :param n:求めたい数
    :return:約数のリスト
    """
    result = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            result.append(i)
            if i != n // i:
                result.append(n // i)
    return result


ans = make_divisor(_n)
ans.sort()
for i in ans:
    print(i)
