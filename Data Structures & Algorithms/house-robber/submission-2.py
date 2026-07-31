class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        prev2 = nums[0]
        prev = max(nums[0], nums[1])
    
        for i in range(2, n):
            if prev == prev2:
                temp = prev
                prev2 = prev
                prev = temp + nums[i]
            elif nums[i] + prev2 > prev:
                temp = prev2
                prev2 = prev
                prev = nums[i] + temp
            elif nums[i] > nums[i - 1]:
                prev += (nums[i] - nums[i - 1])
            else:
                prev2 = prev

        return prev