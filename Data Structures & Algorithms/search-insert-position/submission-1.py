class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        prev = -1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target:
                prev = mid
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid
        return prev if prev != -1 else len(nums)