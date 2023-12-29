import itertools

n = int(input())
p = list(map(int, input().split()))

available_number = []

for i in range(n - 2, -1, -1):
    if p[i + 1] < p[i]:
        j = i - 1
        while p[i] < p[j]:
            j -= 1
            break
        p[i], p[j] = p[j], p[i]
        p[i+1:].reverse()
print(p)
