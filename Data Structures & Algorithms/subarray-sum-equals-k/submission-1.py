class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # prefix sum approach
        res = 0
        prefixSum = {0 : 1}
        currSum = 0

        for i in range(len(nums)):
            currSum += nums[i]
            rem = currSum - k

            if rem in prefixSum:
                res += prefixSum[rem]

            prefixSum[currSum] = prefixSum.get(currSum, 0) + 1

        return res