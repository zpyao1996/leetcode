class Solution:
    #BFS
    def numSquares1(self, n):
        """
        :type n: int
        :rtype: int
        """
        i,numlist=1,[]
        while i**2<=n:
            numlist.append(i**2)
            i+=1
        queue={n}
        count=0
        while queue:
            nextqueue=set()
            count+=1
            for i in queue:
                for k in numlist:
                    if i==k:
                        return count
                    if i>k:
                        nextqueue.add(i-k)
            queue=nextqueue

    #DP?
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans={}
        i=1
        while i**2<=n:
            ans[i**2]=1
            i+=1
        while True:
            newans = {}
            for i in ans:
                for j in ans:
                    if j>=i:
                        if i + j not in ans and i+j<=n:
                            if newans.get(i+j,0):
                                newans[i+j]=min(ans[i]+ans[j],newans[i+j])
                            else:
                                newans[i+j]=ans[i]+ans[j]
            ans.update(newans)
            if ans.get(n,0):
                return ans[n]

sol=Solution()
print(sol.numSquares(12))
