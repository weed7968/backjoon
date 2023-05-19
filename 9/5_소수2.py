M = int(input())
N = int(input())

list = []
for num in range(M, N + 1):
    count = 0
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                count += 1
                break
        if count == 0:
            list.append(num)


if len(list) > 0:
    print(sum(list))
    print(min(list))
else:
    print(-1)
