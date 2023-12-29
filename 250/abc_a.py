h,w = map(int,input().split())
r,c = map(int,input().split())

dx = [0,0,1,-1]
dy = [1,-1,0,0]

#xが縦軸
#yが横軸

count = 0
for i in range(4):
    now_x = r+dx[i]
    now_y = c+dy[i]
    if(0<now_x<=h) and (0<now_y<=w):
        count+=1
print(count)
