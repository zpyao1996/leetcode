class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        numberset=set()
        return self.ishappyhelper(n,numberset)
    def ishappyhelper(self,n,numberset):
        squaresum=0
        while n>0:
            squaresum+=(n%10)**2
            n=n//10
        if squaresum ==1:
            return True
        elif squaresum in numberset:
            return False
        else:
            numberset.add(squaresum)
            return self.ishappyhelper(squaresum,numberset)
sol=Solution()
print(sol.isHappy(19))