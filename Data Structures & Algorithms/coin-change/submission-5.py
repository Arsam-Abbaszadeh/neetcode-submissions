import sys
sys.setrecursionlimit(50000)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # top down... too slow ):
        memo = [None] * (amount + 1)
        # memo = {}
        memo[0] = 0

        def dfs(curr):
            if memo[curr] != None:
                return memo[curr]
            
            mini = float('inf')
            for coin in coins:
                if curr - coin >= 0:
                    mini = min(mini, dfs(curr - coin) + 1)
            
            memo[curr] = mini
            return mini

        res = dfs(amount)
        return res if res != float('inf') else -1
