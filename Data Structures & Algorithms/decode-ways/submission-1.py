class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {}
        def dfs(i):
            if i <= len(s) - 1 and s[i] == '0':
                return 0
            if i == len(s):
                return 0
            if i == len(s) - 1:
                return 1
            if i in dp:
                return dp[i]   

            vari = dfs(i + 1)
            vari1 = 0
            if i + 1 < len(s) and int(s[i] + s[i + 1]) <= 26:
                vari1 = dfs(i + 2)
                if i + 1 == len(s) - 1:
                    vari1 += 1
            dp[i] = vari + vari1
            return vari + vari1
        
        return dfs(0)