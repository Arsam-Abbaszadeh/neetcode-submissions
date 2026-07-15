class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # bit wise operator
        a = 0
        for num in nums:
            a = a ^ num
        b = 0
        for num in range(1, len(nums) + 1):
            b = b ^ num
        return b ^ a