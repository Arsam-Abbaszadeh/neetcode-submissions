class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        start, end = word[0], word[-1]
        dirs = [
            (1, 0), (0, 1),
            (-1, 0), (0, -1)
        ]

        board_r_edge = len(board)
        board_c_edge = len(board[0])  
        word_count = 0
        vis = {}

        def dfs_search(r, c, search_val_i, word_dir):
            nonlocal word_count
            if search_val_i < 0 or search_val_i >= len(word):
                if len(word) == word_count:
                    return True
                return False
            
            if r < 0 or r >= board_r_edge or c < 0 or c >= board_c_edge:
                return False
            
            if board[r][c] == word[search_val_i]:
                word_count += 1
                vis[(r, c)] = True
                for r_c, c_c in dirs:
                    n_r, n_c = r + r_c, c + c_c
                    if (n_r, n_c) not in vis:
                        if dfs_search(n_r, n_c, search_val_i + word_dir, word_dir):
                            return True
                del vis[(r, c)]
                word_count -= 1
            
            return False

        for i in range(board_r_edge):
            for j in range(board_c_edge):
                if board[i][j] == start:
                    if dfs_search(i, j, 0, 1):
                        return True
                elif board[i][j] == end:
                    if dfs_search(i, j, len(word) - 1, -1):
                        return True
        
        return False