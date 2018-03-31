class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s and not t:
            return False
        if s == t:
            return False
        if len(s) < len(t):
            s, t = t, s
        for i in range(len(t)):
            if s[i] == t[i]:
                continue
            else:
                return s[i + 1:] == t[i + 1:] or s[i + 1:] == t[i:]
        return len(s) == len(t)+1

sol=Solution()
print(sol.isOneEditDistance('','a'))