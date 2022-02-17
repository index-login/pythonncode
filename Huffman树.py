def man(shu):
    sum=0
    for i in range(n-1):
        shu.sort()
        value=shu.pop(0)+shu.pop(0)
        sum+=value
        shu.append(value)
    print(sum)
n=int(input())
list_shu=list(map(int,input().split()))
man(list_shu)
