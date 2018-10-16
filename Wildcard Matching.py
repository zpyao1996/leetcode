class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        row, col = len(p), len(s)
        match_matrix = [[0 for _ in range(col+1)] for _ in range(row+1)]
        match_matrix[0][0] = 1
        for i in range(row):
            if p[i] == '*':
                for j in range(col + 1):
                    if match_matrix[i][j] == 1:
                        match_matrix[i + 1][j:] = [1] * (col - j + 1)
                        break
            if p[i] == '?':
                for j in range(col):
                    if match_matrix[i][j] == 1:
                        match_matrix[i+1][j+1] = 1
            else:
                for j in range(col):
                    if match_matrix[i][j] == 1 and p[i] == s[j]:
                        match_matrix[i+1][j+1] =1
        print(match_matrix)
        return match_matrix[row][col] == 1

s = "acdcb"
p = "a*c?b"
# s = "adceb"
# p = "*a*b"
sol=Solution()
print(sol.isMatch(s, p))




