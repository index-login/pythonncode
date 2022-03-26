#数组[1,3,2,4,5]中的数组成连续数组，最高是多少？ 1 3 4 5   最高是4
# def L(nums,i):
#     maxlen=1
#     for j in range(i+1,len(nums)):
#         if nums[j] >nums[i]:
#             maxlen=max(maxlen,  L(nums,j)+1)
#     return maxlen
# a=[1,5,2,4,3]
# print(L(a,0))

# def coins1(arr, aim):
#     def process1(arr, index, aim):
#         if index == len(arr):
#             return 1 if aim == 0 else 0
#         else:
#             res = 0
#             for i in range(0, aim//arr[index]+1):
#                 res += process1(arr, index+1, aim-arr[index]*i)
#         return res
#
#
#     if arr == None or len(arr) == 0 or aim < 0:
#         return 0
#     return process1(arr, 0, aim)


"""
题目：

给定数组arr，arr中所有的值都为正数且不重复。每个值代表一种面值的货币，每种面值的货币可以使用任意张，再给定一个整数aim代表要找的钱数，求换钱有多少种方法。

令arr={5，10，25，1}，aim=1000。

过程：

用0张5元，让{10，25，1}去组成剩下的1000，方法记作res1

用1张5元，让{10，25，1}去组成剩下的995，方法记作res2

用2张5元，让{10，25，1}去组成剩下的990，方法记作res3
……………………

用200张5元，让{10，25，1}去组成剩下的0，方法记作res201

这样得到的每个结果，再用其他面值的货币去组成剩下的钱，利用递归，算出每个结果下剩下的钱有多少种组合，再把这201个结果的组合数相加得到最终的结果数。
"""
#
#
# def m(aim,index,l):
#     """
#     暴力搜索算法
#     :param aim:钱
#     :param index:层数
#     :param l:钱数组
#     :return:多少中方法
#     """
#     res=0
#     if index==len(l):   #递归终止判断
#         if aim==0:
#             res=1
#         else:
#             res=0
#
#     else:
#         t=0
#         for i in range(int(aim//l[index])+1):
#             res+=m(aim-l[index]*i,index+1,l)
#     return res





# zong=[[0 for k in range(mo+1)]for i in range(len(a))]
# def m1(aim,index,l):#1 800
#     """
#     记忆搜索算法
#     :param aim: 钱
#     :param index: 钱 数组/层数
#     :param l: 数组
#     :return: 多少种方法
#     """
#     res=0
#     if index==len(l):
#         return 1 if aim==0 else 0
#     else:
#         t=0
#         #进行 3 90 的情况运算有多少种方法
#         for i in range(int(aim//l[index])+1):
#             t=zong[index][aim-l[index]*i]
#             if t !=0:
#                 res+=0 if t ==-1 else t
#             else:
#                 res+=m1(aim-l[index]*i,index+1,l)
#                             #100        3+1
#                             #zong[2]等于3
#         #循环结束后，返回res
#          #3
#     #表示index-1 才能返回到本次index，剩余aim钱有多少种方法
#     if index !=0:
#         zong[index - 1][aim] = -1 if res == 0 else res
#     return res



a=[5,10,25,1]  #142511
#a=[5,2,3]
mo=1000

def m2(aim,l):
    """
    动态规划

    想到杨辉三角
    有点感觉像杨辉三角的思维
    以l[0]为底部，l[i]里的每一个数基于上一行的数据


    :param aim:
    :param l:
    :return:
    """
    wow=len(l)
    dp=[[0 for _ in range(aim+1)] for i in range(wow)]
    for i in range(wow):
        dp[i][0]=1  #每种货币一次也不兑换时
    for t in range(1,aim//l[0]+1):
        dp[0][l[0]*t]=1   #能完整换货币的金额
    for i in range(1,wow):
        for j in range(aim+1):
            num=0
            for k in range(j//l[i]+1):
                num+=dp[i-1][j-l[i]*k]
            # 当剩余j元时，用了k张l[i]纸币剩余的钱，l[i-1]列表中是否能全兑换,次数都存进num了
            dp[i][j]=num   #统计当剩余j元时，有多少中方法
    print(dp[2])
    return dp[wow-1][aim]  #最后就是顶部，最后剩余aim钱时


print(m2(mo,a))
# print(m1(mo,0,a))
# print(len(zong))

