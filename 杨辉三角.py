def triangles(num):
    n = [1]
    print("1")
    while num > 1:
        n = [1] + [n[i] + n[i+1] for i in range(len(n) - 1)] + [1]
        for i in range(len(n)):
            print(n[i], end=' ') # 将列表转为要求的格式
        print(n,end=' ')
        num -= 1
        print()                  # 换行
# if __name__ == '__main__':
#     n = int(input())
#     triangles(n)

def les(num):
    if 1==num:
        return [1]
    if num>1:
        n=[1,1]
        while(2<num):
            n=[1]+[n[i]+n[i+1] for i in range(len(n)-1)]+[1]
            num-=1
        return n
# for i in range(int(input())):
#     print(les(i+1))

def s(num):
    print("1")
    n=[1]
    while(num>1):
        n=[1]+[n[i]+n[i+1] for i in range(len(n)-1)]+[1]
        print(n)
        for i in range(len(n)):
            print(n[i],end=' ')
        print()
        num-=1
s(5)