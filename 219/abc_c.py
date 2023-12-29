x = list(input())
n = int(input())
s = [input() for _ in range(n)]

dict_ = {}
for i, j in enumerate(x):
    dict_[j] = chr(i + 97)


def _convert_word(target: str) -> str:
    """
    辞書にしたがって文字を変換する
    :param target: 変換する文字
    :return:
    """
    result = ""
    for i in range(len(target)):
        result += dict_[target[i]]
    return result


# 通常の辞書順に変換する
after_converting_s = []
for i in range(n):
    target = s[i]
    converted_word = _convert_word(target)
    after_converting_s.append(converted_word)
after_converting_s.sort()

# dict_のkeyとvalueを入れ替え
dict_ = {v: k for k, v in dict_.items()}

# xの辞書順に戻す
for i in range(n):
    target = after_converting_s[i]
    print(_convert_word(target))
