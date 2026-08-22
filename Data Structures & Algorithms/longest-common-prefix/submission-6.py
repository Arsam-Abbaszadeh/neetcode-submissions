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
            for i in range(limit):
                if prefix_res[: limit - i] == word[: limit - i]:
                    prefix_res = prefix_res[: limit - i]
                    break
                
        return prefix_res
