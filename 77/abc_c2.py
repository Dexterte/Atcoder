n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

"""_summary_
中段を固定して、上<中と中<下をそれぞれ数える。
上<中と中<下は独立した事象なので、それぞれを掛ける
→ TLE
これを二分探索するとACになる
"""

ans = 0
for i in range(n):

    # 上<中の数をカウントする
    small_top_cnt = 0
    # 中<下の数をカウントする
    large_bottom_cnt = 0

    for j in range(n):
        if A[j] < B[i]:
            small_top_cnt += 1
        if B[i] < C[j]:
            large_bottom_cnt += 1
    ans += small_top_cnt*large_bottom_cnt
print(ans)
