class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atlantic, pacific = set(), set()

        ROWS, COLS = len(heights), len(heights[0])

        def dfs(r: int, c: int, prev: int, ocean: set):
            if(
                r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                prev > heights[r][c] or
                (r, c) in ocean
            ):
                return

            ocean.add((r, c))

            curr = heights[r][c]
            dfs(r + 1, c, curr, ocean)
            dfs(r - 1, c, curr, ocean)
            dfs(r, c + 1, curr, ocean)
            dfs(r, c - 1, curr, ocean)
        
        lr, lc = ROWS - 1, COLS - 1

        for r in range(ROWS):
            dfs(r, 0, heights[r][0], pacific)
            dfs(r, lc, heights[r][lc], atlantic)
        
        for c in range(COLS):
            dfs(0, c, heights[0][c], pacific)
            dfs(lr, c, heights[lr][c], atlantic)
        
        return list(atlantic.intersection(pacific))