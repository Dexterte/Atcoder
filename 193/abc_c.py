import math

n = int(input())

s = set()
for i in range(2, int(math.sqrt(n)) + 1):
    x = i * i
    while x <= n:
        s.add(x)
        x *= i
print(n - len(s))
