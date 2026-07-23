class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = nums[0]
        curr2 = curr
        max_sum = curr
        for num in nums[1:]:
            if num >= 0:
                if curr < 0:
                    curr = num
                else:
                    curr += num
                curr2 += num
                temp = max(curr, curr2)
                curr, curr2 = temp, temp
            else:
                max_sum = max(curr, max_sum)
                curr = num
                curr2 += num


        return max(max_sum, curr, curr2)