import math
class Solution:
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        ans=[]
        clist=[]
        self.findhelper(n,2,ans,clist)
        ans.pop()
        return ans
    def findhelper(self,n,i,ans,clist):
        for j in range(i,math.floor(math.sqrt(n))+1):
            if n%j==0:
                clist.append(j)
                self.findhelper(n//j,j,ans,clist)
                clist.pop()
        ans.append(clist+[n])

sol=Solution()
print(sol.getFactors(32))