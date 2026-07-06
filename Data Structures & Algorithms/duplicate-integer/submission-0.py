class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        vals = {}
        for num in nums:
            if num in vals:
                return True
            vals[num] = True
            
        return False