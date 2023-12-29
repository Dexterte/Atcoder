n = int(input())
A = list(map(int, input().split()))

B = [0, 360]
total = 0
for i in range(n):
    total += A[i]
    B.append(total)

diff = []
for i in range(1,n+2):
    diff.append(B[i]-B[i-1])

print(max(diff))
