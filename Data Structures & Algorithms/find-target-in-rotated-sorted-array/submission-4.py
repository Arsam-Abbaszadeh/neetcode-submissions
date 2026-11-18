class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m

            if nums[m] >= nums[l]:
                # left sorted portion
                if target > nums[m] or nums[l] > target:
                    l = m + 1
                else:
                    r = m - 1
            else:
                # right sorted portion
                if nums[m] > target or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1



        return -1