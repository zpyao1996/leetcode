class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        col = len(p) + 1
        row = len(s) + 1
        ans_matrix = [[0 for _ in range(col)] for _ in range(row)]
        ans_matrix [0][0] = 1
        for i in range(0, row):
            for j in range(1, col):
                if  i > 0 and p[j-1] != '*' and ans_matrix[i-1][j-1] == 1:
                    if (p[j - 1].isalpha() and p[j - 1] == s[i - 1]) or p[j - 1] == '.':
                        ans_matrix[i][j] = 1
                elif p[j - 1] == '*' and ans_matrix[i][j-2] == 1:
                    ans_matrix[i][j] = 1
                    if p[j - 2] == '.' :
                        for k in range(i + 1, row):
                            ans_matrix[k][j] = 1
                    else:
                        k = i + 1
                        while k < row and p[j - 2] == s[k - 1]:
                            ans_matrix[k][j] = 1
                            k += 1
        return ans_matrix[row - 1][col - 1] == 1


s = "abbabaaaaaaacaa"
p = "a*.*b.a.*c*b*a*c*"
sol = Solution()
print(sol.isMatch(s, p))