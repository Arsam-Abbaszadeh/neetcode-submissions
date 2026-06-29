"""
Just run binary search...
We are in ascending order. 
So if the number before is bigger, then that's the rotate point. 
From memory we can kind of think about it in the form of Two sorted arrays appended 
If you find the point at which the previous number is bigger or the next number is less, then you know all Numbers that we are looking for before. That are going to be strictly less or more
How do you decide whether to go left or right?



To look at a hint.
Binary search to find split between the two. Arrays so the min. 
Binary search across two segments. 
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) -1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m

            # check if we are in left sorted portion
            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            # right sorted portion 
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return -1