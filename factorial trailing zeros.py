class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        i = 1
        while 5 ** i <= n:
            ans += n // (5 ** i)
            i += 1
        return ans
