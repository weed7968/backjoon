word = input().upper()
arr = list(set(word))
count = []

for i in arr:
    cnt = word.count(i)
    count.append(cnt)

if count.count(max(count))>1:
    print("?")
else:
    result = count.index(max(count))
    print(arr[result])