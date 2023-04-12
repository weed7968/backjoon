word = []
for _ in range(5):
    a = input()
    word.append(a)

result = ''
for i in range(15):
    for j in range(5):
        if i < len(word[j]):
            result += word[j][i]

print(result)