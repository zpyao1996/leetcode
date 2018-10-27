class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if board and board[0]:
            col = len(board[0])
            row = len(board)
        else:
            return
        visited = [[0 for _ in range(col)] for _ in range(row)]
        O_list = [[i, j] for i in range(row) for j in range(col)
                  if board[i][j] == 'O' and (i==0 or i==row-1 or j==0 or j==col-1)]
        while O_list:
            x, y = O_list[0]
            c_list = []
            def DFS(board, visited, x, y, c_list, row, col):
                if not (0<=x<=row-1 and 0<=y<=col-1):
                    return
                if visited[x][y] == 0 and board[x][y] == 'O':
                    visited[x][y] = 1
                    c_list.append([x, y])
                    for a, b in [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]:
                        DFS(board, visited, a, b, c_list, row, col)

            DFS(board, visited, x, y, c_list, row, col)
            for x, y in c_list:
                board[x][y] = '1'
                if [x,y] in O_list:
                    O_list.remove([x,y])
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '1':
                    board[i][j] = 'O'


"""
    def solve(self, board):
        
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        
        if board and board[0]:
            col = len(board[0])
            row = len(board)
        else:
            return
        O_list = [[i, j] for i in range(row) for j in range(col)
                  if board[i][j] == 'O']
        while O_list:
            x, y = O_list[0]
            visited_list = [[x,y]]
            c_list = [[x,y]]
            flag = self.DFS(board, visited_list, c_list, row, col)
            for x, y in visited_list:
                if not flag:
                    board[x][y] = 'X'
                O_list.remove([x,y])

    def DFS(self, board, visited_list, c_list, row, col):
        flag = False
        while c_list:
            cur_x, cur_y = c_list.pop()
            for x, y in [[cur_x, cur_y-1], [cur_x, cur_y+1],
                         [cur_x-1, cur_y], [cur_x+1, cur_y]]:
                if not [x,y] in visited_list:
                    if 0<=x<row and 0<=y<col:
                        if board[x][y] == 'O':
                            visited_list.append([x,y])
                            c_list.append([x,y])
                    else:
                        flag = True
        return flag
"""
board = [['O','O'],
         ['O','O']]
board = [["O","O","O","O","X","X"],["O","O","O","O","O","O"],
         ["O","X","O","X","O","O"],["O","X","O","O","X","O"],
         ["O","X","O","X","O","O"],["O","X","O","O","O","O"]]
sol=Solution()
sol.solve(board)
print(board)