# 入力値の受け取り
n = int(input())

# 約数が8個の数をカウントする
answer = 0

# iを1からNまで2づづ増やす
for i in range(1, n+1, 2):
    # 約数の数をカウントする
    count = 0

    for j in range(1, n+1):
        if i % j == 0:
            count += 1
    if count == 8:
        answer += 1

print(answer)
