for bai in range(1,10):
    for shi in range(10):
        for ge in range(10):
            su=bai*bai*bai+shi*shi*shi+ge*ge*ge
            num=str(bai)+str(shi)+str(ge)
            if str(su)== num:
                print(su)
# 问题描述
# 　　153是一个非常特殊的数，它等于它的每位数字的立方和，即153=1*1*1+5*5*5+3*3*3。编程求所有满足这种条件的三位十进制数。
# 输出格式
# 　　按从小到大的顺序输出满足条件的三位十进制数，每个数占一行

# def is_ans(num):
#     num_sum = pow(int(str(num)[0]), 3) + pow(int(str(num)[1]), 3) + pow(int(str(num)[2]), 3)
#     if num == num_sum:
#         return True
#
# for ans in range(100, 1000):
#     if is_ans(ans):
#         print(ans)