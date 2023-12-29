n = int(input())
c = list(map(int, input().split()))
q = int(input())
s = [input().split() for _ in range(q)]

initial_total = sum(c)

set_sale_count = 0
set_sale_number = 0
all_type_sale_count = 0
all_type_sale_number = 0


for i in range(q):
    if s[i][0] == '1' and c[int(s[i][1]) - 1] > 0:
        c[int(s[i][1]) - 1] -= int(s[i][2])
    elif s[i][0] == '2':

        set_sale_count += 1
        set_sale_number += int(s[i][1])
    elif s[i][0] == '3':
        all_type_sale_count += 1
        all_type_sale_number += int(s[i][1])

for i in range(n):
    if i % 2 == 0:
        c[i] -= set_sale_number * set_sale_count

    c[i] -= all_type_sale_count * all_type_sale_number

print(c)
