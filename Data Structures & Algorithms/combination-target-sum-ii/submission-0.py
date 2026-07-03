class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        sol = []
        def dfs(i, curr, rem):
            if rem == 0:
                sol.append(curr.copy())
                return
            if rem < 0 or i >= len(candidates):
                return
            
            # include current candidate
            curr.append(candidates[i])
            dfs(i + 1, curr, rem - candidates[i])
            curr.pop()
        
            # exlcude duplicates or just exclude current candidate
            while i + 1 < len(candidates) and candidates[i] == candidates[ i + 1]:
                i += 1

            dfs(i + 1, curr, rem)

        dfs(0, [], target)
        return sol