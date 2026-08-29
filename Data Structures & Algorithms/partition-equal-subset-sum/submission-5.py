class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2 != 0:
            return False
        target //= 2

        memo = {}
        def dfs(i, curr):
            if len(nums) == i or (i, curr) in memo:
                return False

            new_total = curr + nums[i]

            if new_total == target:
                return True
            
            keep = False
            if new_total < target:
                keep = dfs(i + 1, new_total)
                
            if keep:
                return True

            skip = dfs(i + 1, curr) 

            if skip or keep:
                return True

            memo[(i, curr)] = False
            return False

        return dfs(0, 0)