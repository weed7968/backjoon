arr = []

for _ in range(9):
    arr.append(list(map(int, input().split())))

x = 0
y = 0
Max = -1

for i in range(9):
    for j in range(9):
        if arr[i][j] > Max:
            Max = arr[i][j]
            x = i + 1
            y = j + 1

print(Max)
print(x, y, end=" ")