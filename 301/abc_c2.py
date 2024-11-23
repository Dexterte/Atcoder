s = input()
t = input()


def map_word_lengths(word):
    """
    文字の数を数えたリストを作成する
    Args:
        word ():

    Returns:

    """
    # 文字の数を持っておく @は26番目
    result = [0 for _ in range(27)]

    for word_i in word:
        if word_i == "@":
            result[26] += 1
        else:
            result[ord(word_i) - ord("a")] += 1
    return result


cs = map_word_lengths(s)
ct = map_word_lengths(t)

for i in range(27):
    target = chr(i + ord("a"))
    if target in "atcoder":
        if cs[i] < ct[i]:
            cs[26] -= ct[i] - cs[i]
        else:
            ct[26] -= cs[i] - ct[i]
    else:
        # atcoderではなく、違いの文字の数がことなればNG
        if cs[i] != ct[i]:
            print("No")
            exit()

if cs[26] < 0 or ct[26] < 0:
    print("No")
    exit()

print("Yes")
