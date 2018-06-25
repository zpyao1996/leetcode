class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        left=0
        right=0
        charset=set()
        cmax=0
        while right<len(s):
            if s[right] in charset:
                charset.remove(s[left])
                left+=1
            else:
                charset.add(s[right])
                right+=1
                cmax=max(cmax,right-left)
        return cmax
sol=Solution()
print(sol.lengthOfLongestSubstring(''))