class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def backtrack(sub, idx):
            if idx == len(nums):
                res.append(sub.copy())
                return

            sub.append(nums[idx])
            backtrack(sub, idx + 1)
            sub.pop() 
            
            while idx < len(nums) - 1 and nums[idx] == nums[idx + 1] :
                idx += 1
            backtrack(sub, idx + 1)
        
        backtrack([], 0)
        return res