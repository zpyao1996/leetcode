from itertools import product
class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return None
        row=len(board)
        col=len(board[0])
        for i in range(row):
            for j in range(col):
                a=[l for l in [i-1,i,i+1] if l>=0 and l<row]
                b=[l for l in [j-1,j,j+1] if l>=0 and l<col]
                neighbors=list(product(a,b))
                neighbors.remove((i,j))
                liveneighbors=sum(map(lambda x: 1 if board[x[0]][x[1]] >0 \
                    else 0,neighbors))
                cstate=board[i][j]
                if cstate==0:
                    if liveneighbors==3:
                        board[i][j]=-1
                if cstate==1:
                    if not liveneighbors in [2,3]:
                        board[i][j]=2
        for i in range(row):
            for j in range(col):
                if board[i][j]==2:
                    board[i][j]=0
                if board[i][j]==-1:
                    board[i][j]=1
a=[[1,1],[1,0]]
sol=Solution()
sol.gameOfLife(a)
print(a)
