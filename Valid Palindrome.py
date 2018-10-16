class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join([x for x in s if x.isalpha() or x.isdigit()]).lower()
        return s[::-1] == s
