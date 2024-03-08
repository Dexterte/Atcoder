s = input()

"""
26進数を10進数に変換すると考える
"""
ans = 0
for i in range(len(s)):
    ans += 26 ** (len(s) - i - 1) * (ord(s[i]) - 64)
print(ans)
