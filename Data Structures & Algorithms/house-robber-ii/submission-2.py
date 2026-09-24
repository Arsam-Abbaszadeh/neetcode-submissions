class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_linear(houses):
            p2, p1 = 0, 0
            for x in houses:
                p2, p1 = p1, max(p1, p2 + x)
            return p1

        return max(nums[0], rob_linear(nums[:-1]), rob_linear(nums[1:]))