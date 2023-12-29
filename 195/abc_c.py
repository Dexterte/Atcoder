n = int(input())

ans = max(n - 999, 0) + max(n - int('9' * 6), 0) + max(n - int('9' * 9), 0) + max(n - int('9' * 12), 0) + max(
    n - int('9' * 15), 0)
print(ans)
