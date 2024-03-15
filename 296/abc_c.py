n, x = map(int, input().split())
a = list(map(int, input().split()))

set_a = set(a)

for i in range(n):
    target = x + a[i]
    if target in set_a:
        print("Yes")
        exit()
print("No")
