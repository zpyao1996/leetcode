class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        clist=set([amount])
        ans=0
        totalset=set([amount])
        while clist:
            newset=set()
            for i in clist:
                if i==0:
                    return ans
                else:
                    for j in coins:
                        remain=i-j
                        if remain>=0 and remain not in totalset:
                            newset.add(remain)
            clist=newset
            totalset=totalset.union(newset)
            ans += 1

        return -1
sol=Solution()
print(sol.coinChange([71,440,63,321,461,310,467,456,361],9298))

