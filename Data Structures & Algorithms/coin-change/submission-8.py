class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #  bottom up non recursive
        memo = [amount + 1] * (amount + 1)
        memo[0] = 0
        for a in range(1, amount + 1):
            for coin in coins:
                if a - coin >= 0:
                    mini = min(memo[a], 1 + memo[a - coin])
                    memo[a] = mini

        return memo[-1] if memo[-1] <= amount else -1