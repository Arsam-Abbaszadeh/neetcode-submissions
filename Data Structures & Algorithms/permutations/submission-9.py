class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(a_set: set, perm: List):
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            
            for i in range(len(nums)):
                if i not in a_set:
                    a_set.add(i)
                    perm.append(nums[i])
                    dfs(a_set, perm)
                    a_set.remove(i)
                    perm.pop()
            
        dfs(set(), [])
        return res