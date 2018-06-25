class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans=0
        for i in s:
            ans*=26
            ans+=i-'A'+1
        return ans
