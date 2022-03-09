def find(li,num):
    r=len(li)
    l=0
    while True:
        mid=(r-l)//2
        if li[mid]>num:
            #左边
            r=mid
        elif li[mid]< num:
            l=mid
        else:
            return mid
a=[1,4,6,7,9,0]
print(find(a,4))