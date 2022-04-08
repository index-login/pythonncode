

def B():
    xList = [i for i in range(2)]
    yList = [i for i in range(3)]
    points = [(x, y) for x in xList for y in yList]
    s = set()
    res = 2 + 3

    def getLine(p, q):
        a = (q[1] - p[1]) / (q[0] - p[0])
        b = (p[0] * (p[1] - q[1]) + p[1] * (q[0] - p[0])) / (q[0] - p[0])
        return a, b

    for p in points:
        for q in points:
            if p != q and p[0] != q[0] and p[1] != q[1]:
                s.add(getLine(p, q))
    print(len(s) + res)
    print(s)
B()