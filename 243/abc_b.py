n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
cnt = 0
for i,j in zip(a,b):
    if i == j:
        cnt+=1
common = set(a) & set(b)
print(cnt)
print(len(common)-cnt)
