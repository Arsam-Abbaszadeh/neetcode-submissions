class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        if not nums:
            return result

        NUMS = len(nums)
        def backtrack(curr, idx, added):
            if added:
                result.append(curr.copy())
            
            if idx < NUMS:
                curr.append(nums[idx])
                backtrack(curr, idx + 1, True)
                curr.pop()
                backtrack(curr, idx + 1, False)
            
        backtrack([], 0, False)
        return result

