class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        rotten = 0
        total = 0
        time = 0
        q = deque()

        for r in range(n):
            for c in range(m):
                if grid[r][c] >= 1:
                    total += 1
                    if grid[r][c] == 2:
                        rotten += 1
                        q.append((r, c))

        while rotten < total:
            made_rotten = False
            for _ in range(len(q)):
                r,c = q.popleft()

                if r > 0 and grid[r - 1][c] == 1:
                    grid[r - 1][c] = 2
                    q.append((r - 1, c))
                    rotten += 1
                    made_rotten = True
                if r < n - 1 and grid[r + 1][c] == 1:
                    grid[r + 1][c] = 2
                    q.append((r + 1, c))
                    rotten += 1
                    made_rotten = True
                if c > 0 and grid[r][c - 1] == 1:
                    grid[r][c - 1] = 2
                    q.append((r, c - 1))
                    rotten += 1
                    made_rotten = True
                if c < m -1 and grid[r][c + 1] == 1:
                    grid[r][c + 1] = 2
                    q.append((r, c + 1))
                    rotten += 1
                    made_rotten = True

            time += 1
            if not made_rotten:
                break
        
        return time if total == rotten else -1