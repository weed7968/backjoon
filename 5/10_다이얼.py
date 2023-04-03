arr = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
word = input()

time = 0

for i in arr:
    for j in word:
        if j in i:
            time += arr.index(i)+3

print(time)