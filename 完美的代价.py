'''
问题描述
回文串，是一种特殊的字符串，它从左往右读和从右往左读是一样的。小龙龙认为回文串才是完美的。现在给你一个串，它不一定是回文的，请你计算最少的交换次数使得该串变成一个完美的回文串。
交换的定义是：交换两个相邻的字符
例如mamad
第一次交换 ad : mamda
第二次交换 md : madma
第三次交换 ma : madam (回文！完美！)
输入格式
第一行是一个整数N，表示接下来的字符串的长度(N <= 8000)
第二行是一个字符串，长度为N.只包含小写字母
输出格式
如果可能，输出最少的交换次数。
否则输出Impossible
样例输入
5
mamad
样例输出
3
'''

#mamammaad  mamamaad m  mamamad am mamaad mam mamadamam
#mamadmmaa  mamadmaa m  mamadma am mamada mam mamadamam
#dmamammaa  mama dmmaa

def is_h(list1):
    count=set([ (list1[i],list1.count(list1[i])) for i in range(len(list1))])
    l=0
    #print(count)
    if len(list1) % 2==1:
        '''字符串是奇数就不能出现奇数的字符
           偶数则就不能出现两次奇数的字符        
        '''
        for i,n in count:
            if n% 2 ==1:
                if l == 1:
                    return False
                l=1
    else:
        for i,n in count:
            if n%2 ==1:
                return False
    return True

n=int(input())
if n%2==0:
    """
    奇数需要再加一次循环
    """
    n//=2
else:
    n//=2
    n+=1
str1=list(input().strip())
setup=0
templist=list()
zhong=list()
if is_h(str1):
    for i in range(n):
        if str1.count(str1[i]) != 1:  #判断出现找不到配对的字符
            s=str1[::-1].index(str1[i])   #采用列表倒序查找配对字符 第几个就是需要几步
            setup+=s
            templist.append(str1.pop(len(str1) - s - 1))
        else:
            setup+=n//2 -i+1
            zhong.append(str1.pop(i))
result = str1 + zhong + templist[::-1]
print("".join(result))
print(setup)