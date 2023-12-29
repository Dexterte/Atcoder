n = int(input())
A = list(map(int, input().split()))
q = int(input())
M = list(map(int, input().split()))

# ビット演算で全探索
def bit_all_search(m):
    # mになるか？
    flag = False
    for bit in range(1 << n):
        total = 0
        for i in range(n):
            if bit & (1 << i):
                total += A[i]
        if total == m:
            flag = True
    return flag


for i in range(q):
    if bit_all_search(M[i]):
        print("yes")
    else:
        print("no")
