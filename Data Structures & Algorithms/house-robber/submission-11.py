class Solution:
    def rob(self, nums: List[int]) -> int:
        # top down
        n = len(nums)
        if n == 1:
            return nums[0]
        memo = [None] * n
        memo[0] = nums[0]
        memo[1] = max(nums[0], nums[1])
        if n == 2:
            return memo[1]
        
        def topdown(i):
            if memo[i] != None:
                return memo[i]

            val = max(topdown(i - 2) + nums[i], topdown(i - 1))
            memo[i] = val
            return val

        return topdown(n - 1)
                
            