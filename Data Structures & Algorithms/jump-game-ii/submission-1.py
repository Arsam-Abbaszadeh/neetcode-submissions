class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        reach end of list with jumps
        this seems like a dp problem where we check if we can reach the end.
        reach end in min jumps, so from each square see how many jumps to reach the end
        0 is infinite.

        since this is max jump we could also keep count of how many squares we can travel, that would be useful for checking if we can make it to the end
        """
        dp = [float('inf')] * len(nums)
        dp[-1] = 0
        for i in range(len(nums) - 2, -1, -1):
            jump = nums[i]
            for j in range(i + 1, min(i + jump + 1, len(nums))):
                dp[i] = min(dp[j] + 1, dp[i])

        return dp[0]
            