n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

"""
全探索する
計算量：O(N**3)→TLE
"""
cnt = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            if A[i] < B[j] < C[k]:
                cnt += 1
print(cnt)

