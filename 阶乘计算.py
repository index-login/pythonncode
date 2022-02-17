def jiecheng(num):
    if num==1:
        return 1
    return num*jiecheng(num-1)
n=int(input())
print(jiecheng(n))