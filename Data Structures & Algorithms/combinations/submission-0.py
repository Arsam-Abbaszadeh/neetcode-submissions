class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        sol = []

        def dfs(i, curr, rem):
            if rem == 0:
                sol.append(curr.copy())
                return
            
            if rem <= n - i:
                # include curr
                curr.append(n - i)
                dfs(i + 1, curr, rem - 1)
                curr.pop()
                dfs(i + 1, curr, rem)
             




        dfs(0, [], k)
        return sol