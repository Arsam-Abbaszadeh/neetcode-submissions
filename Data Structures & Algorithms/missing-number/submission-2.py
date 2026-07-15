class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum(range(1, len(nums) + 1))- sum(nums)
