n = int(input())
a = list(map(int, input().split()))

total = sum(a)
mod = 10 ** 9 + 7

d = 0
for ai in a:
    d += ai * ai
print((total*total - d) // 2 % mod)

