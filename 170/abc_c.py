import bisect

x, n = map(int, input().split())
p = list(map(int, input().split()))

li = [i for i in range(110)]
for pi in p:
    li.remove(pi)

index = bisect.bisect_left(li, x)

if abs(x - li[index]) < abs(x - li[index - 1]):
    print(li[index])
elif abs(x - li[index - 1]) < abs(x - li[index]):
    print(li[index - 1])
else:
    print(li[index - 1])
