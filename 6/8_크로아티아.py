word = input()
arr = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in arr:
    word = word.replace(i , 'a')
print(len(word))