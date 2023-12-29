s = input()
word = ""
words = []

for i in range(len(s)):
    word += s[i]
    is_uppercase_letter = word[0].isupper() and word[-1].isupper()
    if 2 <= len(word) and is_uppercase_letter:
        words.append(word)
        word = ""

words = sorted(words, key=str.lower)

ans = ""
for i in range(len(words)):
    ans += words[i]
print(ans)
