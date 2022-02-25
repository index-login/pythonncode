"""
问题描述
　　平面上有两个矩形，它们的边平行于直角坐标系的X轴或Y轴。对于每个矩形，我们给出它的一对相对顶点的坐标，请你编程算出两个矩形的交的面积。
输入格式
　　输入仅包含两行，每行描述一个矩形。
　　在每行中，给出矩形的一对相对顶点的坐标，每个点的坐标都用两个绝对值不超过10^7的实数表示。
输出格式
　　输出仅包含一个实数，为交的面积，保留到小数后两位。
"""
list_jx_1=list(map(float,input().split()))
list_jx_2=list(map(float,input().split()))
x_1=max(min(list_jx_1[0],list_jx_1[2]),min(list_jx_2[0],list_jx_2[2]))
y_1=max(min(list_jx_1[1],list_jx_1[3]),min(list_jx_2[1],list_jx_2[3]))
#交点矩形中的左下角坐标
x_2=min(max(list_jx_1[0],list_jx_1[2]),max(list_jx_2[0],list_jx_2[2]))
y_2=min(max(list_jx_1[1],list_jx_1[3]),max(list_jx_2[1],list_jx_2[3]))
#交点矩形中的右上角坐标
if x_2 >x_1:
    area=(x_2-x_1)*(y_2-y_1)
    print("%.2f" % area)