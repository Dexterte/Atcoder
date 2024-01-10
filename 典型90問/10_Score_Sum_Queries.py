n = int(input())
class_one_of_points = []
class_two_of_points = []
for i in range(n):
    c, p = map(int, input().split())
    if c == 1:
        class_one_of_points.append(p)
        class_two_of_points.append(0)
    elif c == 2:
        class_two_of_points.append(p)
        class_one_of_points.append(0)
q = int(input())
L = []
R = []
for i in range(q):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)

class_one_of_cumulative_sum = [0 for _ in range(n + 1)]
class_two_of_cumulative_sum = [0 for _ in range(n + 1)]

for i in range(n):
    class_one_of_cumulative_sum[i + 1] = class_one_of_cumulative_sum[i] + class_one_of_points[i]
for i in range(len(class_two_of_points)):
    class_two_of_cumulative_sum[i + 1] = class_two_of_cumulative_sum[i] + class_two_of_points[i]

for left, right in zip(L, R):
    class_one_ans = class_one_of_cumulative_sum[right] - class_one_of_cumulative_sum[left - 1]
    class_two_ans = class_two_of_cumulative_sum[right] - class_two_of_cumulative_sum[left - 1]
    print(class_one_ans, class_two_ans)
