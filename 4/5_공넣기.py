n, m = map(int, input().split())
arr = [0] * n

for _ in range(m) :
    i,j,k = map(int, input().split())
    for idx in range(i, j+1):
        arr[idx-1] = k
for i in range(n):
    print(arr[i], end=' ')