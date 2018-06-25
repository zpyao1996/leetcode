class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows>len(s):
            return s
        index = 0
        ans = [0] * numRows
        for i in range(numRows):
            ans[i]=[s[i]]
            index+=1
        for i in s[numRows:]:
            row=index%(2*(numRows-1))
            row=row if row <numRows else (2*(numRows-1)-row)
            ans[row].append(i)

            index+=1
        for i in range(numRows):
            ans[i]=''.join(ans[i])
        return ''.join(ans)
'''
more clean method
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        L = [''] * numRows
        index, step = 0, 1

        for x in s:
            L[index] += x
            if index == 0:
                step = 1
            elif index == numRows -1:
                step = -1
            index += step

        return ''.join(L)
'''
sol=Solution()
print(sol.convert('paypalishiring',3))
