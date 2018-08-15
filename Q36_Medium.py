class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        col = {}
        grid = {}
        count = 0
        for i in range(len(board)):
            row = []
            for j in range(len(board[0])):
                if board[i][j]!='.':
                    if board[i][j] not in row:
                        row.append(board[i][j])
                    else:
                        return False
                    if j not in col:
                        col[j] = [board[i][j]]
                    else:
                        if board[i][j] not in col[j]:
                            col[j].append(board[i][j])
                        else:
                            return False
                    
                    x, y = i/3, j/3
                    if (x,y) not in grid:
                        grid[x,y]=[board[i][j]]
                    else:
                        if board[i][j] not in grid[x,y]:
                            grid[x,y].append(board[i][j])
                        else:
                            return False
        return True