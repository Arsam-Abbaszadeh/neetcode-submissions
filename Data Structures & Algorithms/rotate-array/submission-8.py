class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k > 0:
            k = k % len(nums)
            temp = []
            # get last k elements which will no go front
            for i in range(len(nums) - k, len(nums)):
                temp.append(nums[i])

            # shift everything before k upto 
            for i in range(len(nums) - k - 1, -1, -1):
                nums[i + k] = nums[i]

            for i in range(len(temp)):
                nums[i] = temp[i]