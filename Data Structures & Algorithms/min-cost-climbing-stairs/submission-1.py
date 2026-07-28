class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [0] * len(cost)
        memo[-1] = cost[-1]
        memo[-2] = cost[-2]
        for i in range(len(cost) - 3, -1, -1):
            memo[i] = cost[i] + min(memo[i + 1], memo[i + 2])


        return min(memo[0], memo[1])