class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        prefix = strs[1]
        loop through 1, n
        """

        prefix = strs[0]
        for word in strs[1:]:
            for i in range(min(len(prefix), len(word))):
                if prefix[i] != word[i]:
                    prefix = prefix[:i]
                    break
            if len(prefix) > len(word):
                prefix = word

        return prefix