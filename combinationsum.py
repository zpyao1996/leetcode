class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        ans=[]
        alist=[]
        numset=set()
        for i in range(1,10):
            numset.add(i)
        self.findhelper(ans,alist,n,k,numset)
        return ans

    def findhelper(self,ans,alist,n,i,numset):
        if i==0 and n==0:
            ans.append(list(alist))
            return
        else:
            for j in numset:
                if (not alist) or j>alist[-1]:
                    numset.remove(j)
                    alist.append(j)
                    self.findhelper(ans, alist, n - j, i - 1, numset)
                    numset.add(j)
                    alist.pop()



sol=Solution()
print(sol.combinationSum3(3,7))



