from collections import defaultdict

s = input()
t = input()

# 文字の数を持っておく @は26番目
cs = [0 for _ in range(27)]
ct = [0 for _ in range(27)]

for si in s:
    if si == "@":
        cs[26] += 1
    else:
        cs[ord(si) - ord("a")] += 1

for ti in t:
    if ti == "@":
        ct[26] += 1
    else:
        ct[ord(ti) - ord("a")] += 1

atcoder_list = [False for _ in range(27)]

for s in "atcoder":
    atcoder_list[ord(s) - ord("a")] = True

for i in range(27):
    # atcoderではなく、違いの文字の数がことなればNG
    if not atcoder_list[i]:
        if cs[i] != ct[i]:
            print("No")
            exit()
    else:
        # 差があれば@を使う
        if cs[i] < ct[i]:
            cs[26] -= ct[i] - cs[i]
        else:
            ct[26] -= cs[i] - ct[i]

if cs[26] < 0 or ct[26] < 0:
    print("No")
    exit()

print("Yes")
