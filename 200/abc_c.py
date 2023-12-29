import math

n = int(input())
a = list(map(int, input().split()))

cnt_list = [0 for _ in range(200)]
for i in range(n):
    cnt_list[a[i] % 200] += 1

ans = 0
for cnt in cnt_list:
    ans += math.comb(cnt, 2)

print(ans)
