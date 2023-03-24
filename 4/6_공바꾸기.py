n, m = map(int, input().split())
arr = list(range(1,n+1))
for _ in range(m):
    a, b= map(int,input().split())
    x = arr[a-1]
    y = arr[b-1]
    arr[a-1] = y
    arr[b-1] = x
for i in range(n):
    print(arr[i], end=" ")