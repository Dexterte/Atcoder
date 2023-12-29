n = int(input())
X, Y = [], []
for i in range(n):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            diff_x1_to_x2 = X[i] - X[j]
            diff_y1_to_y2 = Y[i] - Y[j]
            diff_x1_to_x3 = X[i] - X[k]
            diff_y1_to_y3 = Y[i] - Y[k]
            if diff_x1_to_x2 * diff_y1_to_y3 == diff_y1_to_y2 * diff_x1_to_x3:
                print("Yes")
                exit()
print("No")
