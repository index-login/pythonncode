
#https://www.jianshu.com/p/ec0b97676c3e

# (a^b)%c
a=2
b=400
c=100
ans=1
a%=c
while b!=0:
    if b & 1:  #取b末位二进制位进行操作,末尾为1，res把当前基数算进去
        ans=(ans*a)%c
    a=(a*a)%c
    b>>=1
print(ans)