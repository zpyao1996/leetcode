class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        if n==1:
            return 1
        ans=[0 for _ in range(n+1)]
        ans[0]=1
        ans[1]=1
        for i in range(2,n+1):
            for j in range(0,i):
                ans[i]+=ans[j]*ans[i-j-1]
        return ans[n]

sol=Solution()
print(sol.numTrees(3))
