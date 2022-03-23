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


#
#
# def m(aim,index,l):
#     res=0
#     if index==len(l):
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

a=[5,10,25,1]  #142511
#a=[5,2,3]
mo=1000
zong=[[0 for k in range(mo+1)]for i in range(len(a))]

def m1(aim,index,l):#1 800
    """
    记忆搜索算法
    :param aim: 钱
    :param index: 钱 数组/层数
    :param l: 数组
    :return: 多少种方法
    """
    res=0
    if index==len(l):
        return 1 if aim==0 else 0
    else:
        t=0
        #进行 3 90 的情况运算有多少种方法
        for i in range(int(aim//l[index])+1):
            t=zong[index][aim-l[index]*i]
            if t !=0:
                res+=0 if t ==-1 else t
            else:
                res+=m1(aim-l[index]*i,index+1,l)
                            #100        3+1
                            #zong[2]等于3
        #循环结束后，返回res
         #3
    #表示index-1 才能返回到本次index，剩余aim钱有多少种方法
    if index !=0:
        zong[index - 1][aim] = -1 if res == 0 else res
    return res

print(m1(mo,0,a))
print(len(zong))