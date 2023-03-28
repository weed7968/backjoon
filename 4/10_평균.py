n = int(input())
arr = list(map(int, input().split()))
m = max(arr)
sum = 0

for i in range(n):
    sum += arr[i]/m*100

print(sum/n)
