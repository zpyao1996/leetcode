class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if (not grid) or (not grid[0]):
            return 0
        row, col = len(grid), len(grid[0])
        