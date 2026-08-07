class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        fresh = 0
        time = 0
        q = deque()

        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        while q and fresh > 0:
            for _ in range(len(q)):
                r,c = q.popleft()
                if r > 0 and grid[r - 1][c] == 1:
                    grid[r - 1][c] = 2
                    q.append((r - 1, c))
                    fresh -= 1
                if r < n - 1 and grid[r + 1][c] == 1:
                    grid[r + 1][c] = 2
                    q.append((r + 1, c))
                    fresh -= 1
                if c > 0 and grid[r][c - 1] == 1:
                    grid[r][c - 1] = 2
                    q.append((r, c - 1))
                    fresh -= 1
                if c < m -1 and grid[r][c + 1] == 1:
                    grid[r][c + 1] = 2
                    q.append((r, c + 1))
                    fresh -= 1

            time += 1
        
        return time if fresh == 0 else -1