class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 1:
            return 0
        """
        right non connected bar, water is trapped

        find leftmost
            search for max right most, which is first bar of same height or gearater or just the next greatest length bar
                any bars throughout just subtract there height from the total.

        O(n^2) time, O(1) space

        once we find the largest bar 
        """
        l = r = 0
        water = 0
        while r < len(height):
            # searching for left
            while l < len(height) - 1 and (height[l] == 0 or height[l + 1] >= height[l]):
                l += 1
            if l >= len(height) - 1:
                break
            r = l + 1
            largest = 0 # set in loop
            largest_r = r
            reduce_sf = 0
            reduce = 0
            while r < len(height) and height[l] > height[r]: # removed or r - l < 2
                if height[r] >= largest:
                    largest = height[r]
                    largest_r = r
                    reduce_sf = reduce
                reduce += height[r]
                r += 1

            if r < len(height):
                largest_r = r
                reduce_sf = reduce

            level = min(height[l], height[largest_r])
            width = largest_r - l - 1

            water += level * width - reduce_sf

            l = largest_r
            r = largest_r
        return water
