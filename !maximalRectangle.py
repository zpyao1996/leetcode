class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        cmax=0
        if not matrix or not matrix[0]:
            return 0
        ans=[[[] for _ in range(len(matrix[0]))]for _ in range(len(matrix))]
        if matrix[0][0]=='0':
            ans[0][0]=0
        else:
            ans[0][0]=[0,0]
            cmax=1
        for i in range(1,len(matrix)):
            if matrix[i][0]=='0':
                ans[i][0]=0
            else:
                if not ans[i-1][0]==0:
                    ans[i][0]=ans[i-1][0]
                else:
                    ans[i][0]=[i,0]
                cmax=max(cmax,i-ans[i][0][0]+1)
        for j in range(1,len(matrix[0])):
            if matrix[0][j]=='0':
                ans[0][j]=0
            else:
                if not ans[0][j-1]==0:
                    ans[0][j]=ans[0][j-1]
                else:
                    ans[0][j]=[0,j]
                cmax=max(cmax,j-ans[0][j][1]+1)
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][j]=='0':
                    ans[i][j]=0
                else:
                    ans[i][j]=self.poshelper(ans[i-1][j],ans[i][j-1],i,j)
                    cmax=max(cmax,(i-ans[i][j][0]+1)*(j-ans[i][j][1]+1))
        return cmax
    def poshelper(self,pos1,pos2,i,j):
        if pos1==0 and pos2==0:
            return [i,j]
        if pos1==0:
            return [i,pos2[1]]
        if pos2==0:
            return [pos1[0],j]
        else:
            return


a=[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
sol=Solution()
print(sol.maximalRectangle(a))
