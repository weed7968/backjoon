N, B = input().split()
arr = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
B = int(B)

N = N[::-1]
result = 0

for i in range(len(N)):
    result += arr.index(N[i]) * (B ** i)

print(result)