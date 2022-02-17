# class Solution():
#     def solveNQueens(self, n):
#
#         k = 0
#         ans, q = [], [None] * n
#
#         def dfs(k, n):
#             if k == n:
#                 tmp = []
#                 for i in range(n):
#                     s = ""
#                     for j in range(n):
#                         s += "Q" if q[i] == j else '.'
#                     tmp.append(s)
#                 ans.append(tmp)
#
#             else:
#                 for j in range(n):
#                     if self.place(k, j, q):
#                         q[k] = j
#                         dfs(k + 1, n)
#
#         dfs(k, n)
#         return ans, len(ans)
#
#     def place(self, k, j, q):
#         for i in range(k):
#             if q[i] == j or abs(q[i] - j) == abs(i - k):
#                 return False
#         return True
#
# if __name__ == '__main__':
#     solu = Solution()
#     # solu.solveNQueens(4)
#     print(solu.solveNQueens(4))

# class sol():
#     def solven(self,n):
#         self.helper([-1]*n,0,n)
#     def helper(self,column,rowindex,n):
#         if rowindex == n:
#             self.printsol(column,n)
#             return
#         for colum in range(n):
#             column[rowindex]=colum
#             if self.isvalid(column,rowindex):
#                 self.helper(column,rowindex+1,n)
#     def isvalid(self,column,rowindex):
#         for i in range(rowindex):
#             if column[i] ==column[rowindex]:
#                 return False
#             elif abs(column[i]-column[rowindex]==rowindex-i):
#                 return False
#
#         return True
#
#     def printsol(self,colum,n):
#
#         for i in range(n):
#             line = ''
#             for c in range(n):
#                 if colum[i] ==c:
#                     line +="Q"
#                 else:
#                     line+="0"
#             print(line)
#         print()
# n=sol().solven(4)


# def solve(n):
#     def DFS(result,queen,xy_dif,xy_sum):
#         p=len(queen)
#         if p==n:
#             result.append(queen)
#             return None
#         for q in range(n):
#             if q not in queen and p-q not in xy_dif and p+q not in xy_sum:
#                 DFS(result,queen+[q],xy_dif+[p-q],xy_sum[p+q])
#     result=[]
#     DFS(result,[],[],[])
#     return [ ["." *i + "Q" + "." * (n-i-1) for i in sol] for sol in result]

def solveNQueens(self, n):
    def DFS(valid_configs, queens, yx_diffs, yx_sums):
        """`valid_configs` contains configurations of n queens that satisfy
        threat constraints.

        Each element in `queens` represents the position of a queen.
        Its row is indicated by the element *index* and its column is
        indicated by the element *value*. Given this, duplicate values
        in `queens` would mean two rows had a queen in the same column,
        which isn't allowed.

        yx_diffs and yx_sums both represent diagonals that are threatened
        by a queen in `queens`. As shown below, diagonals can be represented
        with a single integer calculated from the difference or sum of a
        position's row and columns indices. Differences (row - col) are
        left->right diagonals and sums are right->left diagonals.

        yx_diffs (row_idx - col_idx):
        3 |  3  2  1  0
        2 |  2  1  0 -1
        1 |  1  0 -1 -2
        0 |  0 -1 -2 -3
        r  ------------
          c  0  1  2  3

        yx_sums (row_idx + col_idx):
        3 |  3  4  5  6
        2 |  2  3  4  5
        1 |  1  2  3  4
        0 |  0  1  2  3
        r  ------------
          c  0  1  2  3
        """
        row_idx = len(queens)

        if row_idx == n:
            valid_configs.append(queens)
            return

        for col_idx in range(n):
             if not col_idx in queens and not row_idx - col_idx in yx_diffs and not row_idx + col_idx in yx_sums:
                DFS(valid_configs, queens + [col_idx], yx_diffs + [row_idx - col_idx],yx_sums + [row_idx + col_idx])

#  0 q=[0] []

    result = []
    DFS(result, [], [], [])
    #return [["." * i + "Q" + "." * (n - i - 1) for i in sol] for sol in result]
    return [result,queue,]
print(solveNQueens(3,4))