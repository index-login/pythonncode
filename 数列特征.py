def isans(list1):
    print(max(list1),min(list1),sum(list1))
n=int(input())
listnum=list(map(int,input().split()))
isans(listnum[0:n])
