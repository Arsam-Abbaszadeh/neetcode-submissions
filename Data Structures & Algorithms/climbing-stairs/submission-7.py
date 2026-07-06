class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for _ in range(n):
            temp = one
            one = two + one
            two = temp
        
        return two
            