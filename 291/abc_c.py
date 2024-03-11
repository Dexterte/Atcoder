n = int(input())
s = input()

now_x, now_y = 0, 0
visited = set()

for i in range(n):
    visited.add((now_x, now_y))

    if s[i] == "R":
        now_x += 1
    elif s[i] == "L":
        now_x -= 1
    elif s[i] == "U":
        now_y += 1
    elif s[i] == "D":
        now_y -= 1

    if (now_x, now_y) in visited:
        print("Yes")
        exit()
print("No")
