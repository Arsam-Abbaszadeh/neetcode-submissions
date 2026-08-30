class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        given an n x n board, place n queens so that they cant take eachother

        pass more queens to place,
            if n = 0, 
                return True

        for bubling back up, do we try everything else before doing so? if rem = 1, then no but otherwise probs
        """
        # Brute force
        board = [[0] * n for _ in range(n)]
        ans = []
        cols = set()
        def backtrack(r, rem, board):
            if rem == 0:
                fin_board = []
                for i, row in enumerate(board):
                    colStr = []
                    for j, col in enumerate(row):
                        if col == float('inf'):
                            colStr.append('Q')
                        else:
                            colStr.append('.')
                    fin_board.append(''.join(colStr))
                ans.append(fin_board)
                return 

            for c in range(n):
                if c not in cols and board[r][c] == 0:
                    board[r][c] = float('inf')
                    cols.add(c)
                    markBoard(r, c, 1)
                    backtrack(r + 1, rem - 1, board)
                    cols.remove(c)
                    markBoard(r, c, -1)
                    board[r][c] = 0

        def markBoard(r, c, direction):
            for i in range(n):
                # mark diags
                j = i + 1
                if r + j < n and c + j < n:
                    board[r + j][c + j] += direction

                if r - j >= 0 and c - j >= 0:
                    board[r - j][c - j] += direction

                if r + j < n and c - j >= 0:
                    board[r + j][c - j] += direction

                if r - j >= 0 and c + j < n:
                    board[r - j][c + j] += direction

        backtrack(0, n, board)
        return ans   