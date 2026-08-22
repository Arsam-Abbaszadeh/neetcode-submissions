class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        longest common prefix all the wprds
        we need counts 
        """

        prefixes = {}
        for i in range(1, len(strs[0]) + 1):
            prefixes[strs[0][0:i]] = 1

        for word in strs[1:]:
            for i in range(1, len(word) + 1):
                prefix = word[0 : i]
                if prefix in prefixes:
                    prefixes[prefix] += 1

        pre_res = ""
        for prefix, amount in prefixes.items():
            if amount == len(strs) and len(prefix) > len(pre_res):
                pre_res = prefix
        return pre_res
