class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2 != 0:
            return False
        target //= 2

        memo = set()
        def dfs(i, curr):
            if len(nums) == i or (i, curr) in memo:
                return False

            new_total = curr + nums[i]

            if new_total == target:
                return True
            
            if new_total < target and dfs(i + 1, new_total):
                return True 
            
            if dfs(i + 1, curr):
                return True

            memo.add((i, curr))
            return False

        return dfs(0, 0)