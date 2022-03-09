"""
试题 C ：货物摆放本题总分： 10 分
【 问题描述 】
小蓝有一个超大的仓库，可以摆放很多货物。
现在，小蓝有，，箱货物要摆放在仓库，每箱货物都是规则的正方体。
小蓝规定了长、宽、高三个互相垂直的方向，每箱货物的边都必须严格平行于长、宽、高。小蓝希望所有的货物最终摆成一个大的立方体。即在长、宽、高的方向上分别堆 L 、 W 、 H 的货物，满足， , = LxwxH 。
给定 n ，请问有多少种堆放货物的方案满足要求。
例如，当， : = 4 时，有以下 6 种方案： lxlx4 、 lx2x2 、 lx4xl 、 2xlx2 、 2 X 2 XI 、 4 X 1 Xl 。
请问，当 n = 2021041820210418 （注意有 16 位数字）时，总共有多少种方案？
提示：建议使用计算机编程解决问题。
"""

num=0
# import  time
#
# start = time.perf_counter()
a=list()
n=2021041820210418
m=int(2021041820210418**(1/2)) #最小需要两个数乘
for i in range(1,m):
    if n%i==0:
        a.append(i)
        a.append(n//i)
a.sort()
#排列出n的公因数，减少计算机运算，才能算出结果
for i in a:
    for w in a:
        for h in a:
            temp=i*w*h
            if temp == 2021041820210418:
                num+=1
            if temp > 2021041820210418:
                break
print(num)
# end = time.perf_counter()
# print('Running time: %s Seconds' % (end - start))