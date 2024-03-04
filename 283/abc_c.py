s = input()

now = 0
count = 0
while now < len(s):
    if now + 1 < len(s) and s[now:now + 2] == "00":
        now += 2
    else:
        now += 1
    count += 1
print(count)
