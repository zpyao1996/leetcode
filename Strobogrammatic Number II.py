class Solution:
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        nums0=["0","1","8"]
        nums1=["0","1","6","8","9"]
        if n==0:
            return []
        if n==1:
            return nums0
        length=n//2
        orilist=["0","1","6","8","9"]
        for _ in range(length-1):
            newlist=[i+j for i in orilist for j in nums1]
            orilist=list(newlist)
        if n%2==0:
            ans=[i+self.replacestr(i)[::-1] for i in orilist]
        if n%2==1:
            ans=[i+j+self.replacestr(i)[::-1] for i in orilist for j in nums0]
        ans=[i for i in ans if not i[0]=='0']
        return ans

    def replacestr(self,astr):
        astr=astr.replace("6","*")
        astr=astr.replace("9","6")
        astr=astr.replace("*","9")
        return astr

sol=Solution()
print(sol.findStrobogrammatic(4))
