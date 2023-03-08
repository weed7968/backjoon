num = int(input())
p = ''
for i in range(1,num+1):
    p =(" "*(num-i) +  '*'*i)
    print(p)