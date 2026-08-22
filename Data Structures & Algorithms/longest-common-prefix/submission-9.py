class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix_res = strs[0]

        for word in strs[1:]:
            limit = min(len(word), len(prefix_res))
            i = 0
            while i < limit and prefix_res[: limit - i] != word[: limit - i]:
                i += 1
            prefix_res = word[: limit - i]
                
        return prefix_res
