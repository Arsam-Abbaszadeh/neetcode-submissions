class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        curr_sub = []

        def backtrack(i):
            if i == len(nums):
                res.append(curr_sub.copy())
                return
            
            curr_sub.append(nums[i])
            backtrack(i + 1)
            curr_sub.pop()

            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1)
            
        backtrack(0)
        return res

