class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans=[]
        astr=''
        self.restorehelper(s,ans,astr,0)
        for i in range(len(ans)):
            ans[i]=ans[i][1:]
        return ans
    def restorehelper(self,s,ans,astr,num):
        if num==3:
            if int(s)<=255 and (not s[0]=='0' or len(s)==1):
                ans.append(astr+'.'+s)
            else:
                return
        else:
            for i in range(1,len(s)):
                if int(s[:i])<=255 and (not s[0]=='0' or i==1):
                    self.restorehelper(s[i:],ans,astr+('.'+s[:i]),num+1)
sol=Solution()
print(sol.restoreIpAddresses('25525511135'))
