n = int(input())
s = input()

count = 0
max_count = -1
for i in range(n):
    if s[i] == "o":
        count += 1
    else:
        count = 0
    if max_count < count:
        max_count = count

if s.count('o') == n or max_count == 0:
    print(-1)
else:
    print(max_count)
