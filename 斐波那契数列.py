# def f(n):
#     if n <= 1:
#         return n
#     return f(n-1)+f(n-2)
# print(f(35))

#记忆化递归
data=[0] * 10
def f(n):
    if n <= 1:
        return n
    if not data[n]:
        data[n]=f(n-1)+f(n-2)
    return data[n]
print(f(5))