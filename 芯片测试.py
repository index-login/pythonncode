n=int(input())
arr=[list(map(int,input().split()))for i in range(n)]
for i in range(n):
    cun=0
    for j in range(n):
        if arr[j][i]==1:
            cun+=1
        if cun>=n/2:
            print(i+1,end=' ')
