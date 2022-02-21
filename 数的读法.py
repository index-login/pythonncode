shuzi_pinyin= {'0': 'ling', '1': 'yi', '2': 'er', '3': 'san', '4': 'si', '5': 'wu','6': 'liu', '7': 'qi', '8': 'ba', '9': 'jiu'}
shuzi_wei={0:'shi',1:'bai',2:'qian',3:'wan',4:'yi'}
shuzi=input()
number=list()
def dushu(wei):
    wei=list(wei)
    for _ in range(len(wei)):
        if number:
            if "ling" == number[-1] and wei[0] == "0":
                wei.pop(0)
                continue
        number.append(shuzi_pinyin[wei[0]])
        if len(wei) > 3 and "ling" != number[-1]:
            number.append(shuzi_wei[2])
            wei=wei[1:]
            continue
        if len(wei) > 2 and "ling" != number[-1]:
            number.append(shuzi_wei[1])
            wei = wei[1:]
            continue
        if len(wei) > 1 and "ling" != number[-1]:
            if shuzi_pinyin['1'] == number[-1]:
                number.pop()
            number.append(shuzi_wei[0])
            wei = wei[1:]
            continue
        if "ling" == number[-1]:
            wei.pop(0)
    if "ling" == number[-1]:
        number.pop()
n= len(shuzi)
if n > 4:
    if n >8:
        dushu(shuzi[:n-8])
        number.append(shuzi_wei[4])
        dushu(shuzi[n-8:n-4])
        number.append(shuzi_wei[3])
        dushu(shuzi[n-4:])
    else:
        dushu(shuzi[:n-4])
        number.append(shuzi_wei[3])
        dushu(shuzi[n-4:])
else:
    dushu(shuzi)
print(number)