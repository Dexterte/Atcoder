n = int(input())

cnt = 0
for i in range(1, n + 1):
    if not '7' in str(i) and not '7' in oct(i):
        cnt += 1
print(cnt)
