class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        comb = []
        def backtrack(val):
            if len(comb) == k:
                res.append(comb.copy())
                return
            if val == n + 1:
                return

            comb.append(val)
            backtrack(val + 1)
            comb.pop()

            backtrack(val + 1)
        
        backtrack(1)
        return res