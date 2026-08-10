class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        singles = set()
        for num in nums:
            if num in singles:
                return num
            singles.add(num)