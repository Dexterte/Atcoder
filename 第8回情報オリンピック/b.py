from bisect import bisect_left

road_length = int(input())
store_count = int(input())
home_count = int(input())

# 店の位置
store_position = [int(input()) for _ in range(store_count-1)]

# 宅配先の位置
home_position = [int(input()) for _ in range(home_count)]

# 本店の位置を入れる
store_position.append(0)
store_position.append(road_length)

# ソートする
store_position.sort()

"""_summary_

店舗までの距離を二分探索する

"""


ans = 0
for i in range(home_count):

    idx = bisect_left(store_position, home_position[i])

    # 宅配先から店舗までの最短距離
    min_distance = min(abs(store_position[idx-1]-home_position[i]), abs(store_position[idx]-home_position[i]))
    ans += min_distance

print(ans)
