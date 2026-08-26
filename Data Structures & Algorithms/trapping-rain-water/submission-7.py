class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 1:
            return 0

        l = r = 0
        water = 0

        while r < len(height):

            while (
                l < len(height) - 1
                and (height[l] == 0 or height[l + 1] >= height[l])
            ):
                l += 1

            if l >= len(height) - 1:
                break

            r = l + 1

            largest = 0
            largest_r = r

            reduce_sf = 0
            reduce = 0

            while r < len(height) and height[l] > height[r]:

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

            # This is the important bit if you insist on
            # keeping `while r < len(height)` as the outer condition.
            #
            # r may have scanned all the way to len(height),
            # while largest_r is much earlier.
            #
            # So reset r to the boundary we actually chose.
            r = largest_r

        return water