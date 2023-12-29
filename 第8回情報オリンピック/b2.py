road_length = int(input())
store_count = int(input())
home_count = int(input())

# 店の位置
store_position = [int(input()) for _ in range(store_count-1)]

# 宅配先の位置
home_position = [int(input()) for _ in range(home_count)]

"""_summary_

全探索する　→　TLE
各宅配先から全ての店舗までの距離を調べる。

"""

# 本店の位置を入れる
store_position.append(0)
store_position.append(road_length)

ans = 0
for i in range(home_count):
    min_dis = 10**9
    for j in range(store_count+1):
        dis = abs(home_position[i]-store_position[j])
        min_dis = min(dis, min_dis)
    ans += min_dis
print(ans)
