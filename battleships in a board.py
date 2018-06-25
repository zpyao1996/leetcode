class Solution:
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        if not board:
            return 0
        counts=0
        adj=0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=='X':
                    counts+=1
                    if i+1<len(board) and board[i+1][j]=='X':
                        adj+=1
                    if j + 1 < len(board[0]) and board[i][j+1] == 'X':
                        adj += 1
        return counts-adj
