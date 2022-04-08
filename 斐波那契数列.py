def f(n):
    if n <= 1:
        return n
    return f(n-1)+f(n-2)


import  time
start = time.perf_counter()
#记忆化递归
data=[0] * 2000
def f1(n):
    if n <= 1:
        return n
    if not data[n]:
        data[n]=f1(n-1)+f1(n-2)
    return data[n]
end = time.perf_counter()

def fib(n):
    a=b=1
    for i in range(3,n):
        sum=a+b
        a=b
        b=sum
    return sum

print('Running time: %s Seconds' % (end - start))
print(fib(500))