x_1, y_1, x_2, y_2 = map(int,input().split())
judge = False
for i in range(x_1-2,x_1+3):
    for j in range(y_1-2,y_1+3):
        if (x_1-i)**2+(y_1-j)**2 == 5 and (x_2-i)**2+(y_2-j)**2 == 5:
            judge = True
print("Yes") if judge else print("No")
