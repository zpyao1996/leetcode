class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        maxlen=min(list(map(len,strs)))
        if maxlen==0:
            return ''
        for i in range(maxlen):
            flag=True
            for j in range(1,len(strs)):
                if strs[j][i]!=strs[0][i]:
                    flag=False
                    break
            if not flag:
                break
        if flag:
            i+=1
        return strs[0][:i]
sol=Solution()
print(sol.longestCommonPrefix(['abc']))
