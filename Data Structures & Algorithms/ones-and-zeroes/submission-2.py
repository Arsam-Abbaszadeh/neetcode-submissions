class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # Top down DP approach
        memo = defaultdict(int) # m, n, i
        def dfs(i, cm, cn):
            if (i, cm, cn) in memo:
                return memo[(i, cm, cn)]
            if i == len(strs) or cm == m and cn == n:
                return 0
            
            chm , chn = mnCount(strs[i])
            nm, nn = cm + chm, cn + chn
            add = 0
            if nm <= m and nn <= n:
                add = dfs(i + 1, nm, nn) + 1

            skip = dfs(i + 1, cm , cn)

            memo[(i, cm, cn)] = max(skip, add)
            return max(skip, add)

        def mnCount(s: str) -> tuple[int, int]:
            m = n = 0
            for c in s:
                if c == '0':
                    m += 1
                else:
                    n += 1
            return m, n

        dfs(0, 0, 0)
        # return memo[(len(strs) - 1, m, n)]
        return max(memo.values())