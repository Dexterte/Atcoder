n, t = map(int, input().split())
a = list(map(int, input().split()))

one_circle = sum(a)
t %= one_circle

start_sec = 0
for i in range(n):
    end_sec = start_sec + a[i]
    if start_sec <= t <= end_sec:
        print(i + 1, t - start_sec)
        exit()
    start_sec += a[i]
