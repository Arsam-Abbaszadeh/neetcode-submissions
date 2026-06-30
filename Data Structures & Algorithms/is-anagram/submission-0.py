class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = [0] * 26
        s2 = [0] * 26

        for c in s:
            s1[ord(c) - 97] += 1

        for c in t:
            s2[ord(c) - 97] += 1

        for i in range(26):
            if s1[i] != s2[i]:
                return False
        
        return True
