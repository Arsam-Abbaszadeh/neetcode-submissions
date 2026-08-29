class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dfs(i, cur):
            if i == len(nums):
                return 1 if cur == target else 0

            if (i, cur) in memo:
                return memo[(i, cur)]
            
            sub = dfs(i + 1, cur - nums[i])
            add = dfs(i + 1, cur + nums[i])

            memo[(i, cur)] = add + sub
            return add + sub
        
        return dfs(0, 0)
        