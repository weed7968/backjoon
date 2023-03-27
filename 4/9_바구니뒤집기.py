n, m = map(int, input().split())
arr = list(range(1,n+1))
for _ in range(m):
    i, j = map(int,input().split())
    a = arr[i-1:j]
    a.reverse()
    arr[i-1:j] = a
for i in range(n):
    print(arr[i], end=" ")