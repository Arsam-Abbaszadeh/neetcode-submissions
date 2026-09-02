class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #  brute force approach
        n = len(prices)
        # dp = [[0] * n for _ in range(n)]
        dp = {}
        maxProfit = 0

        def dfs(i, hold):
            if i == n:
                return 0
            if (i, hold) in dp:
                return dp[(i, hold)]
            nonlocal maxProfit
            localProfit = 0

            if hold != None and prices[hold] < prices[i]:
                #  you can sell
                profit = prices[i] - prices[hold]
                sell = dfs(i + 1, None)
                localProfit = profit + sell
            elif not hold:
                # try buying
                localProfit = dfs(i + 1, i)

            #  do nothing, ie hold or dont buy
            nothing = dfs(i + 1, hold)
            maxProfit = max(maxProfit, nothing, localProfit)
            dp[(i, hold)] = max(localProfit, nothing)
            return max(localProfit, nothing)

        
        dfs(0, None)
        return maxProfit