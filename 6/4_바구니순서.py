n, m = map(int, input().split())
arr = list(range(1,n+1))
for _ in range(m):
    i, j, k = map(int, input().split())
    arr = arr[:i-1] + arr[k-1:j] + arr[i-1:k-1] + arr[j:]
for i in range(n):
    print(arr[i], end=" ")