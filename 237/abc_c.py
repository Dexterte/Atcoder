s=list(input())
n = len(s)
left = 0
right = n-left-1
while left < right and s[left]=="a" and s[right] =="a":
    left+=1
    right-=1
while left < right and s[right] == "a":
    right-=1
while left < right and s[left]==s[right]:
    left+=1
    right-=1
print("Yes") if right <= left else print("No")
