import math

a, b, h, m = map(int, input().split())

# 角度を求める
h_angle = ((60 * h + m) / 720) * 360
m_angle = m / 60 * 360

# 座標を求める
hy_coordinate = a * math.sin(math.radians(h_angle))
hx_coordinate = a * math.cos(math.radians(h_angle))

my_coordinate = b * math.sin(math.radians(m_angle))
mx_coordinate = b * math.cos(math.radians(m_angle))

ans = math.sqrt((hx_coordinate - mx_coordinate) ** 2 + (hy_coordinate - my_coordinate) ** 2)
print(ans)
