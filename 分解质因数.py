"""
问题描述
　　求出区间[a,b]中所有整数的质因数分解。
输入格式
　　输入两个整数a，b。
输出格式
　　每行输出一个数的分解，形如k=a1*a2*a3...(a1<=a2<=a3...，k也是从小到大的)(具体可看样例)
"""
a,b=map(int,input().split())
def fenjie(num):
    yin=2
    if num < 2:
        return print(num,"=",num)
    print(num, "=", end='')
    while 1 != num:
        if num % yin == 0:
            num //= yin  #取整数
            if num == 1:
                print(yin, end='')
            else:
                print(yin, "*", end='')
        else:
            yin+=1
for i in range(a,b+1):
    fenjie(i)
    print()