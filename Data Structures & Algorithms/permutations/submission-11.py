class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        
        res = []
        def backtrack(curr, i):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            for j in range(i + 1):
                curr.insert(j, nums[i])
                backtrack(curr, i + 1)
                curr.pop(j)
                
        backtrack([], 0)
        return res