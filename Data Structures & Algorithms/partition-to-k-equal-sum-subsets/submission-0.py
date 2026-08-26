class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target = sum(nums) / k
        if target != (target // 1):
            return False
        
        subsets = [0] * k
        def backtrack(i):
            if i == len(nums):
                return True
            
            for j in range(k):
                if subsets[j] + nums[i] <= target:
                    subsets[j] += nums[i]
                    if backtrack(i + 1):
                        return True
                    subsets[j] -= nums[i]
                    
                    if subsets[j] == 0:
                        return False
            return False
        
        return backtrack(0)