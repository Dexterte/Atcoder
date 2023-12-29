n = int(input())
coordinate = []
for i in range(n):
    x, y = map(int, input().split())
    coordinate.append((x, y))


def _is_triangle(a: tuple, b: tuple, c: tuple) -> bool:
    """
    三点を結んだ時に三角形になるか
    :param a:
    :param b:
    :param c:
    :return: true:三角形になる false:三角形にならない
    """
    dx_a_to_b = b[0] - a[0]
    dy_a_to_b = b[1] - a[1]
    dx_a_to_c = c[0] - a[0]
    dy_a_to_c = c[1] - a[1]
    return dx_a_to_b * dy_a_to_c != dx_a_to_c * dy_a_to_b


ans = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if _is_triangle(coordinate[i], coordinate[j], coordinate[k]):
                ans += 1
print(ans)
