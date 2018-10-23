class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        col, row = len(word2) + 1, len(word1) + 1
        ans_matrix = [[-1 for _ in range(col)] for _ in range(row)]
        for i in range(col):
            ans_matrix[0][i] = i
        for i in range(row):
            ans_matrix[i][0] = i
        for i in range(1, row):
            for j in range(1, col):
                if word1[i - 1] == word2[j - 1]:
                    ans_matrix[i][j] = min(ans_matrix[i-1][j-1],
                ans_matrix[i-1][j] + 1, ans_matrix[i][j-1] + 1)
                else:
                    ans_matrix[i][j] = min(ans_matrix[i - 1][j - 1] + 1,
                    ans_matrix[i - 1][j] + 1, ans_matrix[i][j - 1] + 1)
        return ans_matrix[-1][-1]

sol=Solution()
print(sol.minDistance('horse', 'ros'))
