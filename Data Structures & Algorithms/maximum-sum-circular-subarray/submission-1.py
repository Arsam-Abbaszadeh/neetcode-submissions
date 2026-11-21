class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # keep track of the max contigious
        # keep track of min contigious
        # then max is either max contigious or sum(nums) - min contigious
        total = 0

        max_cont = float('-inf')
        curr_max = float('-inf')

        min_cont = float('inf')
        curr_min = float('inf')

        for num in nums:
            total += num

            # kadanes max
            if num > curr_max + num:
                curr_max = num
            else:
                curr_max += num
            max_cont = max(curr_max, max_cont)
        
            # kadanes min
            if num < curr_min + num:
                curr_min = num
            else:
                curr_min += num
            min_cont = min(curr_min, min_cont)
        
        if total == min_cont:
            return max_cont
        return max(total - min_cont, max_cont)

            

