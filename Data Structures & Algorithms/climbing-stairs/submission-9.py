class Solution:
    def climbStairs(self, n: int) -> int:
        # trying to do a bottom up approach
        if n <= 2:
            return n
        steps = n + 1
        memo = [0] * steps
        memo[steps - 1] = 1
        def dfs(curr):
            # 1 step
            total = 0

            if curr + 2 < steps:
                if memo[curr + 2] == 0:
                    dfs(curr + 2)
                total += memo[curr + 2]

            if curr + 1 < steps:
                if  memo[curr + 1] == 0:
                    dfs(curr + 1)
                total += memo[curr + 1]

            memo[curr] = total
        dfs(0)
        return memo[0]

