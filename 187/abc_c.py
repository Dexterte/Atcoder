n = int(input())
s = [input() for i in range(n)]

s_set = set(s)

for i in range(n):
    target = '!' + s[i]
    if target in s_set:
        print(s[i])
        exit()
print('satisfiable')
