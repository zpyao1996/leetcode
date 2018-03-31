class Solution(object):
    def maximalSquare(self, matrix):
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
            ans[0][0]=1
            cmax=1
        for i in range(1,len(matrix)):
            if matrix[i][0]=='0':
                ans[i][0]=0
            else:
                ans[i][0]=1
                cmax=1
        for j in range(1,len(matrix[0])):
            if matrix[0][j]=='0':
                ans[0][j]=0
            else:
                ans[0][j]=1
                cmax=1
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][j]=='0':
                    ans[i][j]=0
                else:
                    if ans[i-1][j]==0 or ans[i][j-1]==0 or ans[i-1][j-1]==0:
                        ans[i][j]=1
                    else:
                        ans[i][j]=min(ans[i-1][j],ans[i-1][j-1],ans[i][j-1])+1
                    cmax=max(cmax,ans[i][j]**2)
        return cmax

a=[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
sol=Solution()
print(sol.maximalSquare(a))