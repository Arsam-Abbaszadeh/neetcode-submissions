class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = [True] * len(nums)
        def dfs(i):
            nonlocal memo
            if i + 1 >= len(nums):
                return True
            
            for j in range(nums[i], 0, -1):
                if memo[i] and dfs(i + j):
                    return True

            memo[i] = False
            return False

        return dfs(0)