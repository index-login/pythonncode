def ans(n,m):
    g=[chr(65+i) for i in range(m)]
    for i in range(n):
        num=list(g[1:i+1]) #行数来表示取几个字母
        listone=num[::-1]+g[:m-i]
        print(listone)
line,num=map(int,input().split())
ans(line,num)

# def is_ans(n, m):
#     graph = [[0 for j in range(m)] for i in range(n)]
#     for i in range(n):
#         for j in range(m):
#             if j >= i:
#                 graph[i][j] = chr(ord('A')+ j - i)
#             else:
#                 graph[i][j] = chr(ord('A') + i - j)
#     return graph
# if __name__ == '__main__':
#     n, m = map(int, input().split())
#     gragh = is_ans(n ,m)
#     for i in range(n):
#         for j in range(m):
#             print(gragh[i][j], end='')
#         print()