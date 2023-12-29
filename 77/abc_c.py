from bisect import bisect_left,bisect_right

n = int(input())
upside = list(map(int, input().split()))
middle = list(map(int, input().split()))
bottom = list(map(int, input().split()))

"""_summary_
abc_c2.pyを二分探索したバージョン
二分探索で、上段<中段の数を数える
二分探索で、中段<下段の数を数える
"""
# ソートする
upside.sort()
middle.sort()
bottom.sort()

ans = 0

for i in range(n):
    upside_than_middle_large_count = bisect_left(upside,middle[i])
    middle_than_bottom_large_count = n-bisect_right(bottom,middle[i])
    ans += upside_than_middle_large_count * middle_than_bottom_large_count
print(ans)
