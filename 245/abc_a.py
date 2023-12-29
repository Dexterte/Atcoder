a,b,c,d =map(int,input().split())

def makeTwoDligts(h,m):
    #mが一桁であればmの前に0をつける
    if(m<10):
        m="0"+str(m)
    return str(h)+str(m)

takahashi = makeTwoDligts(a, b)+"00"
aoki = makeTwoDligts(c, d)+"01"

print("Aoki") if aoki < takahashi else print("Takahashi")
