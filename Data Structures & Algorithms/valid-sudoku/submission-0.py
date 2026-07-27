class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows and cols
        for i in range(9):
            vals_row = [0] * 9
            vals_col = [0] * 9
            for j in range(9):
                if board[i][j] != '.':
                    idx = int(board[i][j]) - 1
                    if vals_row[idx] > 0:
                        return False
                    else:
                        vals_row[idx] += 1
                
                if board[j][i] != '.':
                    idx = int(board[j][i]) - 1
                    if vals_col[idx] > 0 and i != j:
                        return False 
                    else:
                        vals_col[idx] += 1
            
            # check 3 x 3 slots
            for i in range(3):
                for j in range(3):
                    vals = [False] * 9
                    for k in range(3):
                        for l in range(3):
                            row = (i * 3) + k
                            col = (j * 3) + l
                            if board[row][col] != '.':
                                idx = int(board[row][col]) - 1
                                if vals[idx]:
                                    return False
                                else:
                                    vals[idx] = True
        return True
