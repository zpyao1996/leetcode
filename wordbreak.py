''' not effective enough

class Solution(object):
    ans=False
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        self.breakhelper(s,wordDict)
        return self.ans

    def breakhelper(self,s,wordDict):
        if not s:
            self.ans=True
        for i in wordDict:
            if s[0:len(i)]==i:
                self.breakhelper(s[len(i):],wordDict)
'''
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        length=len(s)
        ans=length*[False]
        for i in range(length):
            for astr in wordDict:
                if i+1-len(astr)==0:
                    if s[:len(astr)]==astr:
                        ans[i]=True
                if i+1-len(astr)>0 and ans[i-len(astr)]:
                    if s[i+1-len(astr):i+1]==astr:
                        ans[i]=True
        return ans[length-1]
a="leetcode"
b=["leet","code"]
sol=Solution()
print(sol.wordBreak(a,b))