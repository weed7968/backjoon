n = int(input())
for _ in range(n):
    num, string = input().split()
    result = ""
    for i in string:
        result += i*int(num)
    print(result)