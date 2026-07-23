class Solution:
    def canJump(self, nums: List[int]) -> bool:
        stack = [0]
        while stack:
            cur = stack.pop()
            if cur + 1 >= len(nums):
                return True
                
            for i in range(1, nums[cur] + 1):
                stack.append(cur + i)



        return False