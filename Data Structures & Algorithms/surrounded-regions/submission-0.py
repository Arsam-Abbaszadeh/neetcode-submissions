class Solution:
    def solve(self, board: List[List[str]]) -> None:
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        placeholder = 'T'

        def bfs(coord):
            q = deque([coord])
            x, y = coord
            board[x][y] = placeholder
            while q:
                x, y = q.popleft()
                for cx, cy in dirs:
                    nx = x + cx
                    ny = y + cy
                    if (nx >= 0 and nx < len(board) and ny >= 0 and ny < len(board[0])):
                        if board[nx][ny] == 'O':
                            q.append((nx, ny))
                            board[nx][ny] = placeholder

        for r in [0, len(board) - 1]:
            for c in range(len(board[0])):
                if board[r][c] == 'O':
                    bfs((r, c))
        
        for c in [0, len(board[0]) - 1]:
            for r in range(len(board)):
                if board[r][c] == 'O':
                    bfs((r, c))

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == placeholder:
                    board[r][c] = 'O'