class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxleft = [0] * n 
        maxright = [0] * n
        maxleft[0] = height[0]
        maxright[-1] = height[-1]
        for i in range(1, n):
            curr_max = max(maxleft[i - 1], height[i])
            maxleft[i] = curr_max
        for i in range(n - 2, -1, -1):
            curr_max = max(maxright[i + 1], height[i])
            maxright[i] = curr_max

        res = 0
        for i in range(n):
            res += min(maxleft[i], maxright[i]) - height[i]
        return res

