n, w = map(int, input().split())
cheeses = []
for i in range(n):
    a, b = map(int, input().split())
    # (美味しさ,チーズのグラム数)
    cheeses.append((a, b))

cheeses = sorted(cheeses, key=lambda x: x[0], reverse=True)

ans = 0
for i in range(n):
    if cheeses[i][1] <= w:
        ans += cheeses[i][1] * cheeses[i][0]
        w -= cheeses[i][1]
    elif w < cheeses[i][1]:
        ans += w * cheeses[i][0]
        break
print(ans)
