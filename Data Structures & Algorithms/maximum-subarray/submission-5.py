class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSoFar = nums[0]
        curr = 0
        for n in nums:
            curr = max(curr, 0)
            curr += n
            maxSoFar = max(curr, maxSoFar)
        return maxSoFar