class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if not len(s3) == len(s1) + len(s2):
            return False
        row = len(s1) + 1
        col = len(s2) + 1
        ans_matrix = [[0 for _ in range(col)] for _ in range(row)]
        ans_matrix[0][0] = 1
        for i in range(0, row):
            for j in range(0, col):
                if i > 0 and ans_matrix[i - 1][j] == 1 and s1[i - 1] == s3[i + j - 1]:
                    ans_matrix[i][j] = 1
                elif j > 0 and ans_matrix[i][j - 1] == 1 and s2[j - 1] == s3[i + j - 1]:
                    ans_matrix[i][j] = 1
        return ans_matrix[-1][-1] == 1
