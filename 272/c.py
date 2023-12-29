n = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)

even = []
odd = []
for i in range(n):
    if a[i] % 2 == 0 and len(even) < 2:
        even.append(a[i])
    if a[i] % 2 == 1 and len(odd) < 2:
        odd.append(a[i])

if len(even) < 2 and len(odd) < 2:
    print(-1)
else:
    print(max(sum(even), sum(odd)))
