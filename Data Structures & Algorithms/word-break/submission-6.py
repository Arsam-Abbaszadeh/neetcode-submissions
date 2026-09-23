class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        n = len(s)
        hashDict = set(wordDict)
        # cache for rejecting dfs call at index i
        dontAttemptDp = set()

        def dfs(idx):
            if idx == n:
                return True

            for i in range(idx, n):
                if i not in dontAttemptDp and s[idx: i + 1] in hashDict:
                    if dfs(i + 1):
                        return True
                    else:
                        dontAttemptDp.add(i)

            return False

        return dfs(0)