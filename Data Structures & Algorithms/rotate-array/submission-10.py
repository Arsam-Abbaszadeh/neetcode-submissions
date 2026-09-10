class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # reverse whole array an then reverse then reverse 0 - (k - 1) and k - (n - 1)
        nums.reverse()
        k = k % len(nums)
        def swapSubArray(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        swapSubArray(0, k - 1)
        swapSubArray(k, len(nums) - 1)
        
    