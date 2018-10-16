class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        num_days = len(prices)
        ans_matrix = [[0 for _ in range(num_days + 1)] for _ in  range(k+1)]
        for row in range(1, k+1):
            for col in range(2, num_days + 1):
                possible_list = [ans_matrix[row-1][i] + prices[col-1]
                                 - min([prices[j] for j in range(i,col-1)])
                                 for i in range(col-1)]
                ans_matrix[row][col] = max(possible_list)
        return max([max(i) for i in ans_matrix])

sol=Solution()
k = 2
prices = [3,2,6,5,0,3]
print(sol.maxProfit(k, prices))