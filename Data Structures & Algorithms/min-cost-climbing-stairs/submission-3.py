class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [0] * len(cost)
        prev = cost[-1]
        prev2 = cost[-2]
        for i in range(len(cost) - 3, -1, -1):
            # memo[i] = cost[i] + min(memo[i + 1], memo[i + 2])
            temp = prev2
            prev2 = cost[i] + min(prev2, prev)
            prev = temp

        return min(prev, prev2)