# data = list(map(int, input().split()))
# rabbit = turtle = 0
# time = 0 #目前的时间
# flag = False
# while True:
#     if  rabbit == data[-1] or turtle == data[-1]: # 到达终点
#         break
#     if  rabbit - turtle >= data[2]:
#         for i in range(data[3]):
#             turtle += data[1]
#             time += 1
#             if turtle >= data[-1]:
#                 flag = True
#                 break
#         if flag:
#             break
#
#     time   += 1
#     rabbit += data[0]
#     turtle += data[1]
#
# if rabbit > turtle:  # 谁先到达终点，谁的距离大
#     print('R')
#     print(time)
# elif rabbit < turtle:
#     print('T')
#     print(time)
# else:  # 相等则平局
#     print('D')
#     print(time)

v1,v2,t,s,l=list(map(int,input().split()))
l1=l2=tt = 0
while l1<l and l2<l:

    if l1 - l2 >= t:
        if l2 + v2 * s > l:
            tt += (l - l2) / v2
            l2 = l
        else:
            l2 = l2 + v2 * s
            tt += s
    else:
        l1 += v1
        l2 += v2
        tt += 1

else:
    print(l1,l2)
    if l1==l2==l:
        print("D")
    elif l2>l1:
        print("T")
    else:
        print("R")
    print(tt)