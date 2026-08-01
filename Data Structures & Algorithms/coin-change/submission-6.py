import sys
sys.setrecursionlimit(50000)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # bottom up
        memo = [None] * (amount + 1)
        memo[amount] = 0
        def dfs(curr):
            if curr > amount:
                return float('inf')

            if memo[curr] != None:
                return memo[curr]
                
            mini = float('inf')
            for coin in coins:
                mini = min(mini, dfs(curr + coin) + 1)
            
            memo[curr] = mini
            return mini
            
        dfs(0)
        return memo[0] if memo[0] != float('inf') else -1
         