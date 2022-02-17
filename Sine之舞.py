def _An(n):
    #3
    #( (sin(1)+3)  sin(1-sin(2))+2)  sin(1-sin(2+sin(3)))+1
    #sin(1-sin(2+sin(3)))  3
    #sin(1-sin(2))         2
    #sin(1)                1
    if n>1:
        str1 = str(n)
        while n >1:
            str1 = "sin(" + str1 + ")"
            n-=1
            if n % 2 == 0:
                str1 = str(n) + "+" + str1
            else:
                str1 = str(n) + "-" + str1
        else:
            str1="sin(" + str1 + ")"
    else:
        str1="sin(1)"
    return str1
def _Sn(n):
    i = 1
    str1=_An(i)+str(n)
    while n>1:
        i+=1
        n-=1
        str1="("+str1+")"+_An(i)+"+"+str(n)
    print(str1)
_Sn(3)