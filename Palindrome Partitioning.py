class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        alist=[]
        ans=[]
        self.partionhelper(s,alist,ans)
        return ans

    def partionhelper(self,s,alist,ans):
        if len(s)==0:
            ans.append(list(alist))
        if len(s)==1:
            ans.append(list(alist+[s]))
            return
        else:

            for i in range(1, len(s)+1):
                if self.ispalindrome(s[0:i]):
                    self.partionhelper(s[i:],alist+[s[0:i]],ans)

    def ispalindrome(self,astr):
        if astr==astr[::-1]:
            return True
        else:
            return False
astr="aab"
sol=Solution()
print(sol.partition(astr))
