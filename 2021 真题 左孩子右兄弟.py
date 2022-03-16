"""
试题 H ：左孩子右兄弟时 I ' ed 限制： 1 . 0s 内存限制： 256 . OMB 本题总分： 20 分
【 问题描述 】
对于一棵多义树，我们叮以通过“左孩子右兄弟”表不法，将其转化成一棵二叉树。
如果我们认为每个结点的子结点是无序的，那么得到的二叉树可能不唯一。
换句话说，每个结点可以选任意子结点作为左孩子，并按任意顺序连接右兄弟。
给定一棵包含 N 个结点的多叉树，结点从 1 至 N 编号，其中 1 号结点是根，
每个结点的父结点的编号比自己的编号小。请你计算其通过“左孩子右兄弟”表示法转化成的二叉树，
高度最高是多少。注：只有根结点这一个结点的树高度为 O
。例如如下的多叉树：

 可能有以下 3 种（这里只列出 3 种，并不是全部）不同的“左孩子右兄弟’ ' 表示：
"""

def tree_input(num):
    tree=[[] for _ in range(num+1)]
    for i in range(2,num+1):
        tree[int(input())].append(i)
    return tree
Tree=tree_input(n)
def dfs(x):
    size=len(Tree[x])
    ans=0
    for i in range(size):
        ans=max(ans,dfs(Tree[x][i]))
    return ans+size
print(dfs(1))
