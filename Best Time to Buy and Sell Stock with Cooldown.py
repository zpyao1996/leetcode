class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        length=len(prices)
        diff=[0]*length
        ans=[[0]*length for _ in range(2)]
        for i in range(1,length):
            diff[i]=prices[i]-prices[i-1]
            ans[0][i]=max(ans[0][i-1],ans[1][i-1])
            ans[1][i]=max(ans[1][i-1]+diff[i],ans[0][i-2]+diff[i])

        return max(ans[0][-1],ans[1][-1])
sol=Solution()
print(sol.maxProfit([1,3,2,4]))