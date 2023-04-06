n = int(input())
for _ in range(n):
    arr = list(map(int, input().split()))
    avg = sum(arr[1:])/arr[0]
    count = 0
    for score in arr[1:]:
        if score > avg:
            count += 1
    rate = count / arr[0] * 100
    print(f'{rate:.3f}%')