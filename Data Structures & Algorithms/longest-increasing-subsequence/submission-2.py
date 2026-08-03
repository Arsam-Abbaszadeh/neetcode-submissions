class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # DFS with DP
        dp = [None] * len(nums)
        dp[-1] = 1
        n = len(nums)
        def dfs(i):
            if i >= len(nums):
                return # did not contribute to the length of the longest subsequence
            if dp[i] != None:
                return

            joined_seq = False
            for j in range(i + 1, n):
                dfs(j)
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i] or 0, dp[j] + 1)
                    joined_seq = True
            if not joined_seq:
                dp[i] = 1

        dfs(0)
        return max(dp)