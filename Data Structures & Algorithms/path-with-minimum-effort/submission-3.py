from _heapq import heappop, heappush
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        vis = set()
        moves = [(0, 0, 0)] # (diff, r, c)

        while moves:
            diff, r, c = heappop(moves)
            if r == ROWS - 1 and c == COLS - 1:
                return diff

            if (r, c) in vis:
                continue
            vis.add((r, c))
            h = heights[r][c]

            for cr, cc in dirs:
                nr = r + cr
                nc = c + cc
                if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or (nr, nc) in vis:
                    continue
                
                new_diff = max(diff, abs(h - heights[nr][nc]))
                heappush(moves, (new_diff, nr, nc))

