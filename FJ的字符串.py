n=int(input())
if n==1:
    print("A")
else:
    str1="A"
    for i in range(n-1):
        str1=str1+chr(66+i)+str1
        print(str1)