import itertools
class Solution:
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        count,even,odd,halfnums={},[],[],[]
        ans=[]
        for i in s:
            count[i]=count.get(i,0)+1
        if len(count)==1:
            return [s]
        for i in count:
            halfnums.extend([i for _ in range(count[i] // 2)])
            if count[i]%2==0:
                even.append(i)
            else:
                odd.append(i)
        if len(odd)>1:
            return []
        for j in set(itertools.permutations(halfnums)):
            alist=j+(odd[0],)+j[::-1] if odd else j+j[::-1]
            astr=''.join(alist)
            ans.append(astr)
        return ans

sol=Solution()
a="aaaaaaaaaaaaaaaaa"
print(sol.generatePalindromes(a))
