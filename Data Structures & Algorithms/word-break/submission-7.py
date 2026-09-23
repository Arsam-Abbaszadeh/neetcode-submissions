class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words_counts = set([len(word) for word in wordDict])
        words = set(wordDict)
        memo = {}

        def dfs(i):
            if i > len(s) or i in memo:
                return False
            if i == len(s):
                return True

            for count in words_counts:
                if s[i: i + count] in words and dfs(i + count):
                    return True
                    
            memo[i] = False
            return False
                    
        return dfs(0)