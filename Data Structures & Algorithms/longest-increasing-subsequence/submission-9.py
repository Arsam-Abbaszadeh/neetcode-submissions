class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n

        for i in range(0, n):
            sublen = 0
            for j in range(i - 1, -1, -1):
                if nums[i] > nums[j]:
                    sublen = max(sublen, dp[j])
            dp[i] = sublen + 1


        return max(dp)