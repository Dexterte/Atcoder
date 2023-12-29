n, m = map(int, input().split())
A = [input() for _ in range(2 * n)]
# [人i,勝利数]
rank_table = [[i, 0] for i in range(2 * n)]


def judge(a: str, b: str) -> int:
    """
    :param a:
    :param b:
    :return: 0:aの勝ち 1:bの勝ち -1:引き分け
    """
    if a == b:
        return -1
    if a == 'P' and b == 'G':
        return 0
    if a == 'G' and b == 'C':
        return 0
    if a == 'C' and b == 'P':
        return 0
    return 1


for i in range(m):
    for j in range(n):
        player = rank_table[2 * j][0]
        player_2 = rank_table[2 * j + 1][0]
        result = judge(A[player][i], A[player_2][i])
        if result != -1:
            winner = 2 * j + result
            rank_table[winner][1] += 1
    rank_table = sorted(rank_table, key=lambda x: (-x[1], x[0]))

for i, _ in rank_table:
    print(i + 1)
