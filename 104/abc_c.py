D, G = map(int, input().split())
P = []
C = []
for i in range(D):
    p, c = map(int, input().split())
    P.append(p)
    C.append(c)

ans = 10**9
for bit in range(1 << D):
    # i番目の問題を全て解いた時の点数
    s = 0
    # 解いた問題数
    solved_num = 0
    # ボーナス問題を解かなっかた時のi番目の最大数
    rest_max = -1
    for i in range(D):
        # ボーナスを取った場合
        if bit & (1 << i):
            s += 100*(i+1)*P[i]+C[i]
            solved_num += P[i]
        else:
            rest_max = i
    if s < G:
        sl = 100*(rest_max+1)
        # G点に到達するまでに必要な問題数
        need = (G-s+sl-1)//sl
        if P[rest_max] <= need:
            continue
        solved_num += need
    ans = min(ans, solved_num)
print(ans)
