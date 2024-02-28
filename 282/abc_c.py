n = int(input())
s = list(input())

ans = ""
count = 0
for i in range(n):
    if s[i] == '"':
        count += 1

    if count % 2 == 0 and s[i] == ',':
        ans += '.'
    else:
        ans += s[i]

print(ans)
