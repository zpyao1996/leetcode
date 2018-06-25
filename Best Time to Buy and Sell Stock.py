class Solution(object):
    '''
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        length=len(prices)
        low=[0]*length
        clow=prices[0]
        for i in range(length):
            if prices[i]<clow:
                clow=prices[i]
            low[i]=clow
        high=[0]*length
        chigh=prices[-1]
        for i in range(length-1,-1,-1):
            if prices[i]>chigh:
                chigh=prices[i]
            high[i]=chigh
        return max(map(lambda x:x[0]-x[1],zip(high,low)))
    '''
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxcur=0
        maxsofar=0
        for i in range(1,len(prices)):
            maxcur=max(0,maxcur+prices[i]-prices[i-1])
            maxsofar=max(maxcur,maxsofar)
        return maxsofar
sol=Solution()
print(sol.maxProfit([7,1,5,3,6,4]))
