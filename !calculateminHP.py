class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        [col,row]=[len(dungeon),len(dungeon[0])]
        ans=col*[row*[0]]

        #initial first col
        ans[0][0]=dungeon[0][0]
        for i in range(1,row):
            ans[0][i]=ans[0][i-1]+dungeon[0][i]
        for i in range(1,col):
            for j in range(0,row):
                if j==0:
                    ans[i][j]=ans[i-1][j]+dungeon[i][j]
                else:
                    ans[i][j]=max(ans[i-1][j],ans[i][j-1])+dungeon[i][j]
        a=ans[col-1][row-1]
        if a>0:
            a=0
        return -a
