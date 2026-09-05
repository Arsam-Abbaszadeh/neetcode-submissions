class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dictionary = set(dictionary)
        dp = {}
        def dfs(i, j):
            if j > len(s) or i == len(s):
                return 0
            if i in dp:
                return dp[i]

            #  2 sets of decisions. Choose to skip and choose not to skip
            keep = 0
            if s[i : j] in dictionary:
                keep = dfs(j, j + 1) + (j - i)
            
            expand = dfs(i, j + 1)

            skip = dfs(i + 1, i + 2)
            dp[i] = max(expand, keep, skip)
            return max(expand, keep, skip)
        
        return len(s) - dfs(0, 1)
