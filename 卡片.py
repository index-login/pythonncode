"""
试题 A ：卡片本题总分： 5 分 【 问题描述 】 小蓝有很多数字卡片，每张卡片上都是数字 O 到 9 。
小蓝准备用这些卡片来拼一些数，他想从 1 开始拼出正整数，每拼一个，就保存起来，卡片就不能用来拼其它数了。
小蓝想知道自己能从 l 拼到多少。
例如，当小蓝有 30 张卡片，其中 0 到 9 各 3 张，则小蓝可以拼出 1 到 10 ,但是拼 n 时卡片 1 己经只有一张了，
不够拼出 n 。现在小蓝手里有 0 到 9 的卡片各 2021 张，共 20210 张，请问小蓝可以从 1 拼到多少？
提示：建议使用计算机编程解决问题。

1最先用完
"""
num=0
for i in range(1,100000):
    if '1' in str(i):
        num+=str(i).count("1")
    if num>2021:
        print(i-1)
        break