class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [None] * len(nums)
        dp[-1] = 1
        n = len(nums)
        for i in range(n - 2, -1, -1):
            joined_seq = False
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    joined_seq = True
                    dp[i] = max(dp[i] or 1, dp[j] + 1)
            if not joined_seq:
                dp[i] = 1

        return max(dp)