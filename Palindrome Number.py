class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        z,y = x,0

        while z > 0:
            y = y*10+z%10
            z = z//10

        return y==x


