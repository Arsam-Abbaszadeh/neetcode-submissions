class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        sol = []
        def backtrack(curr, rem, i):
            if i >= len(nums):
                return
            cont = rem - nums[i]

            if cont > 0:
                copy = curr.copy()
                copy.append(nums[i])
                backtrack(copy, cont, i)
                backtrack(curr, rem, i+1)
            elif cont < 0:
                backtrack(curr, rem, i+1)
            else:
                backtrack(curr, rem, i+1)
                copy = curr.copy()
                copy.append(nums[i])
                sol.append(copy)

        
        backtrack([], target, 0)
        return sol

