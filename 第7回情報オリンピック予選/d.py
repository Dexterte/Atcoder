m = int(input())
Mx = []
My = []
for i in range(m):
    x,y=map(int,input().split())
    Mx.append(x)
    My.append(y)
n = int(input())
Nx = []
Ny = []
for i in range(n):
    x,y=map(int,input().split())
    Nx.append(x)
    Ny.append(y)

#並行移動する移動量
Dis = []

#探したい星座を一つ決めて、星座の写真との移動量を測る
for i in range(n):
    dx = Nx[i]-Mx[0]
    dy = Ny[i]-My[0]
    Dis.append([dx,dy])

#探したい星座をDis分だけ並行移動させ、全ての星座が星座の写真にあるものを探す
for i in range(n):
    cnt = 0
    for j in range(m):
        dx = Mx[j]+Dis[i][0]
        dy = My[j]+Dis[i][1]
        if dx in Nx and dy in Ny:
            cnt += 1
        if cnt == m:
            print(Dis[i][0],Dis[i][1])
            exit()
