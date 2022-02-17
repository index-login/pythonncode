num=int(input())
list_num=list(map(int,input().split()))
n=int(input())
def isnum(list1):
    for i in range(num):
        if n == list1[i]:
            print(i + 1)
            break
    else:
        print("-1")
isnum(list_num)


# try:
#     print(list_num.index(n))
# except ValueError:
#     print("-1")
