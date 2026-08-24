class Solution:
    def arrangeCoins(self, n: int) -> int:
        budget = n
        stair_level = 0
        while budget >= stair_level + 1:
            budget -= stair_level + 1
            stair_level += 1
        return stair_level