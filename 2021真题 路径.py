"""
试题 D ：路径本题总分： 1 0分
【 问题描述 】
小蓝学习了最短路径之后特别高兴，他定义了一个特别的图，希望找到图中的最短路径。小蓝的图由 2021 个结点组成，依次编号 1 至 2021 。
对于两个不同的结点 a , b ，如果 a 和 b 的差的绝对值大于 21 ，则两个结点之间没有边相连；
如果 a 和 b 的差的绝对值小于等于 21 ，则两个点之间有二条长度为 a 和 b 的最小公倍数的无向边相连。
例如：结点 1 和结点 23 之间没有边相连；结点 3 和结点 24 之间有一条无向边，长度为 24 ；
结点 15 和结点 25 之间有一条无向边，长度为 75 。请计算，结点 1 和结点 2021 之间的最短路径长度是多少
。提示：建议使用计算机编程解决问题。

"""

def lcm(a ,b):
    if b> a: a, b = b, a
    ab = a * b
    while b > 0:
        b, a = a % b, b  #a%b余c，c为0的话，则c为a，b的最大公约数
    return ab // a  #a，b乘积 除以 最大公约数就是最小公倍数
print(lcm(4,2))

n = 2021
dp = [float('inf')] * (n + 1)

for i in range(1, 22):
    dp[i] = i

for i in range(22, n + 1):
    for j in range(1, 22):
        dp[i] = min(dp[i], dp[i - j] + lcm(i - j, i))

print(dp[n])

# 10266837




a=list()
# def gcp(a, b):
#     while(b%a!=0):
#         a,b=b%a,a
#     return a
for i in range(1,2022):
    for k in range(i,2022):
        if abs(i-k) <=   21:
            temp = 1
            while temp %i != 0 and temp %k != 0 :

                # if 0== temp %i:
                #     if 0== temp%k:
                #         break
                temp+=1
            #temp=gcp(i,k)
            a.append(temp)
# print(min(a))
# def test(a,b):
#     temp=1
#     while True:
#         if temp %i == 0 or temp %k == 0 :
#             return temp
#         temp+=1