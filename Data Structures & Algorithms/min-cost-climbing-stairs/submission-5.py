class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev = cost[-1]
        prev2 = cost[-2]
        for i in range(len(cost) - 3, -1, -1):
            temp = prev2
            prev2 = cost[i] + min(prev2, prev)
            prev = temp

        return min(prev, prev2)