word = input()
word1 = "".join(list(reversed(word)))
if word == word1:
    print(1)
else:
    print(0)