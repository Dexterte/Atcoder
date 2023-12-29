from operator import contains


n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))


def binary_search(key):
    S.sort()
    left = 0
    right = n
    while left < right:
        mid = (left+right)//2
        if S[mid] == key:
            return True
        elif key < S[mid]:
            right = mid
        else:
            left = mid+1
    return False


cnt = 0
for i in range(q):
    if binary_search(T[i]):
        cnt += 1
print(cnt)
