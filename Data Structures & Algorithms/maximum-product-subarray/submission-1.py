class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMax = 1
        curMin = 1

        for num in nums:
            if num == 0:
                curMax = 1
                curMin= 1
                continue

            temp = curMax * num
            curMax = max(num, curMax * num, curMin * num)
            curMin = min(num, temp, curMin * num)
            res = max(res, curMax)
        
        return res