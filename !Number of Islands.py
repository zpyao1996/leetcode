from functools import reduce
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if (not grid) or (not grid[0]):
            return 0
        row, col = len(grid), len(grid[0])
        pos_list = [[i, j] for i in range(row) for j in range(col)
                    if grid[i][j] == '1']
        visited = [[0 for _ in range(col)] for _ in range(row)]
        def get_neighbor(pos, row, col):
            x, y = pos
            ans_list = [[x - 1, y], [x + 1, y],
                        [x, y - 1], [x, y + 1]]
            if x == 0:
                ans_list.remove([x - 1, y])
            if x == row - 1:
                ans_list.remove([x + 1, y])
            if y == 0:
                ans_list.remove([x, y - 1])
            if y == col - 1:
                ans_list.remove([x, y + 1])
            return ans_list
        num_island = 0
        while pos_list:
            x, y = pos_list.pop()
            visited[x][y] = 1
            new_pos_list = list(pos_list)
            pos_queue = list([[x, y]])
            while pos_queue:
                new_pos_queue = reduce(lambda x, y: x + y,
                    map(lambda x: get_neighbor(x, row, col), pos_queue))
                new_pos_queue = list(filter(lambda x:
                    grid[x[0]][x[1]] == '1'
                    and visited[x[0]][x[1]] == 0, new_pos_queue))
                def remove_duplicated(list_list):
                    new_list = list()
                    for a in list_list:
                        if a not in new_list:
                            new_list.append(a)
                    return new_list
                new_pos_queue = remove_duplicated(new_pos_queue)
                for pos_x, pos_y in new_pos_queue:
                    visited[pos_x][pos_y] = 1
                    new_pos_list.remove([pos_x, pos_y])
                pos_queue = new_pos_queue
            pos_list = new_pos_list
            num_island += 1
        return num_island

grid = ['11110',
'11010',
'11000',
'00001']

sol = Solution()
print(sol.numIslands(grid))