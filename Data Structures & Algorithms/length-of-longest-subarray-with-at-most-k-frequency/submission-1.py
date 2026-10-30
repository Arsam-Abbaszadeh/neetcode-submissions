class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        start = 0
        longest = 0
        char_counts = {}

        for end in range(len(nums)):
            char_counts[nums[end]] = char_counts.get(nums[end], 0) + 1

            while char_counts[nums[end]] > k:
                char_counts[nums[start]] -= 1
                start += 1

            longest = max(longest, end - start + 1)

        return longest