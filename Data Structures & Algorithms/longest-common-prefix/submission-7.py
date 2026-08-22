class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        longest common prefix all the wprds
        we need counts 
        """

        prefix_res = strs[0]
        if not prefix_res:
            return ''

        for word in strs[1:]:
            if not word or word[0] != prefix_res[0]:
                return ''

            limit = min(len(word), len(prefix_res))
            i = 0
            while i < limit and prefix_res[: limit - i] != word[: limit - i]:
                i += 1
            prefix_res = word[: limit - i]
                
        return prefix_res
