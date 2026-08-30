class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for _ in range(n)]
        ans = []
        cols = set()
        posDiag = set()
        negDiag = set()

        def backtrack(r, board):
            if r == n:
                ans.append(["".join(r) for r in board])
                return 

            for c in range(n):
                p_diag = c + r
                n_diag = c - r
                if c not in cols and p_diag not in posDiag and n_diag not in negDiag:
                    board[r][c] = 'Q'
                    cols.add(c)
                    negDiag.add(n_diag)
                    posDiag.add(p_diag)

                    backtrack(r + 1, board)

                    cols.remove(c)
                    negDiag.remove(n_diag)
                    posDiag.remove(p_diag)
                    board[r][c] = '.'

        backtrack(0, board)
        return ans   