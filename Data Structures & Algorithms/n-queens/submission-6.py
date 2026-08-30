class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [[0] * n for _ in range(n)]
        ans = []
        cols = set()
        posDiag = set()
        negDiag = set()

        def backtrack(r, rem, board):
            if rem == 0:
                fin_board = []
                for i, row in enumerate(board):
                    colStr = []
                    for j, col in enumerate(row):
                        if col == 1:
                            colStr.append('Q')
                        else:
                            colStr.append('.')
                    fin_board.append(''.join(colStr))
                ans.append(fin_board)
                return 

            for c in range(n):
                p_diag = c + r
                n_diag = c - r
                if c not in cols and p_diag not in posDiag and n_diag not in negDiag:
                    board[r][c] = 1
                    cols.add(c)
                    negDiag.add(n_diag)
                    posDiag.add(p_diag)

                    backtrack(r + 1, rem - 1, board)

                    cols.remove(c)
                    negDiag.remove(n_diag)
                    posDiag.remove(p_diag)
                    board[r][c] = 0

        backtrack(0, n, board)
        return ans   