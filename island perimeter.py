class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        islands=0
        adjacents=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    islands+=1
                    if i+1<len(grid) and grid[i+1][j]:
                        adjacents+=1
                    if j+ 1 < len(grid[0]) and grid[i][j+1]:
                        adjacents += 1
        return islands*4-adjacents*2

