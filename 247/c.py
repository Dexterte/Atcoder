n = int(input())


def connect_str(n: int) -> str:
    if n == 1:
        return str(1)
    return connect_str(n - 1) + " " + str(n) + " " + connect_str(n - 1)


print(connect_str(n))
