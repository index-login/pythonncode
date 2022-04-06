"""
小明被劫持到X赌城，被迫与其他3人玩牌。

一副扑克牌（去掉大小王牌，共52张），均匀发给4个人，每个人13张。

这时，小明脑子里突然冒出一个问题：

如果不考虑花色，只考虑点数，也不考虑自己得到的牌的先后顺序，自己手里能拿到的初始牌型组合一共有多少种呢？

请填写该整数，不要填写任何多余的内容或说明文字。
"""

ans=0
c=list()
def dfs(num,a):
    global ans
    if len(a)>13:return
    if 13 < num or len(a)==13:
        if len(a) ==13:
            ans+=1
            return
        return

    else:
        for i in range(5):
            dfs(num+1,a+[num]*i)
dfs(1,c)
print(ans)