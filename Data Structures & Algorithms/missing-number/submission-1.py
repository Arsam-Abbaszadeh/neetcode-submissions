class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # O(n) space Solution
        nums_dict = {}
        for num in nums:
            nums_dict[num] = True
        
        for i in range(len(nums) + 1):
            if i not in nums_dict:
                return i

        return 0
