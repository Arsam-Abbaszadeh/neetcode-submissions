class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in nums:
                curr = 1
                while num + curr in nums:
                    curr += 1
                longest = max (curr, longest)
        return longest