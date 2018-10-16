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

board = [['O','O'],
         ['O','O']]

sol=Solution()
sol.solve(board)
print(board)