n = int(input())
count = 0
for _ in range(n):
    result = True
    word = input()
    for i in range(len(word)-1):
        if word[i] != word[i+1]:
            if word[i] in word[i+1:]:
                result = False
                break
    if result:
        count += 1
print(count)