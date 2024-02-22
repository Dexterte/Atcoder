h, w = map(int, input().split())
s = [input() for _ in range(h)]
t = [input() for _ in range(h)]


s_col_list = [''.join(ss) for ss in zip(*s)]
t_col_list = [''.join(tt) for tt in zip(*t)]

s_col_list.sort()
t_col_list.sort()

for s_col, t_col in zip(s_col_list, t_col_list):
    if s_col != t_col:
        print("No")
        exit()
print("Yes")
