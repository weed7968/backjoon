arr = list(range(1,31))
for _ in range(28):
    n = int(input())
    arr.remove(n)

print(min(arr))
print(max(arr))
