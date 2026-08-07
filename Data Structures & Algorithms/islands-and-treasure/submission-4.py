class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n, m = len(grid), len(grid[0])
        land = 2 ** 31 - 1

        q = deque()
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 0:
                    q.append((r, c))

        dist = 0
        while q:
            level = len(q)
            for _ in range(level):
                r, c = q.popleft()
                if grid[r][c] in (land, 0):
                    grid[r][c] = dist
                    if r > 0 and grid[r - 1][c] == land:
                        q.append((r - 1, c))
                    if r < n - 1 and grid[r + 1][c] == land:
                        q.append((r + 1, c))
                    if c > 0 and grid[r][c -1] == land:
                        q.append((r, c - 1))
                    if c < m - 1 and grid[r][c + 1] == land:
                        q.append((r, c + 1))

            dist += 1                