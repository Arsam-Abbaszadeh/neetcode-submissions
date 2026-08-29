class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # borrom up loop approach
        memo = [defaultdict(int) for _ in range(len(nums) + 1)]
        memo[0][0] = 1

        for i in range(len(nums)):
            for total, count in memo[i].items():
                memo[i + 1][total + nums[i]] += count
                memo[i + 1][total - nums[i]] += count
        
        return memo[len(nums)][target]
