def ispal(num):
    num=str(num)
    return num==num[::-1]

def sumsum(num):
    return sum(map(int,list(str(num))))
    # for i in range(len(num)):
    #     a+=(int(num[i]))
n=int(input())
for i in range(10000,1000000):
    if ispal(i) and sumsum(i)== n:
        print(i)