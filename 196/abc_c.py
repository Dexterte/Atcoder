from bisect import bisect_right

n = int(input())

list_ = [str(i) * 2 for i in range(1, 10 ** 6)]
list_ = [int(i) for i in list_]
print(bisect_right(list_, n))
