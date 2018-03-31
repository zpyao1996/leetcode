class Solution(object):
    def reverse(self,x):
        """
        :type x: int
        :rtype: int
        """

        if x > 0:
            sign = 1
        else:
            sign = -1
        x = x*sign
        y = 0
        while x > 0:
            y = y * 10 + x % 10
            x = x // 10

        return sign*y
