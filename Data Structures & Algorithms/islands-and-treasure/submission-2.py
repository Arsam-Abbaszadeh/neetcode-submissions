class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n, m = len(grid), len(grid[0])
        avoid = (-1, 0)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    dist = 0
                    q = deque([(i ,j)])
                    while q:
                        level = len(q)
                        for _ in range(level):
                            r, c = q.popleft()
                            if (grid[r][c] == 0 and dist <= grid[r][c]
                                or grid[r][c] != -1 and dist < grid[r][c]) :
                                grid[r][c] = dist
                                if r > 0:
                                    q.append((r - 1, c))
                                if r < n - 1:
                                    q.append((r + 1, c))
                                if c > 0:
                                    q.append((r, c - 1))
                                if c < m - 1:
                                    q.append((r, c + 1))
                        dist += 1
                            

