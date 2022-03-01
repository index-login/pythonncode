"""
问题描述
　　给定一个N阶矩阵A，输出A的M次幂（M是非负整数）
　　例如：
　　A =
　　1 2   1  2
　　3 4   3  4
　　A的2次幂
　　7 10
　　15 22
输入格式
　　第一行是一个正整数N、M（1<=N<=30, 0<=M<=5），表示矩阵A的阶数和要求的幂数
　　接下来N行，每行N个绝对值不超过10的非负整数，描述矩阵A的值
输出格式
　　输出共N行，每行N个整数，表示A的M次幂所对应的矩阵。相邻的数之间用一个空格隔开

"""
n,m=map(int,input().split())
r=moban=[ list(map(int,input().split())) for _ in range(n)]
"""
n*m m*p =n*p
"""

def j(r):

    p=len(moban[0])
    result = [[0 for _ in range(p)] for _ in range(n)]
    for j in range(n):
        # result行
        for k in range(p):
            # reslut列
            for k1 in range(p):
                """
                1 2 3  1 2 3
                4 5 6  4 5 6
                """
                result[j][k] += r[j][k1] * moban[k1][k]

    return result
if m>2:
    result1 = j(r)
    for i in range(m-2):
        result1=j(result1)
else:
    result1=j(r)

for i in result1:
    for t in i:
        print(t,end=' ')
    print()