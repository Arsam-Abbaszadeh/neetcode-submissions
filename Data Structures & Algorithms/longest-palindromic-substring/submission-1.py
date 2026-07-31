class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = (0, 0)
        resLen = 1

        for i in range(len(s)):
            r, l = i, i
            while r < len(s) and l >= 0 and s[r] == s[l]:
                if r - l  + 1> resLen:
                    resLen = r - l + 1
                    res = (l, r)
                l -= 1
                r += 1

            l, r = i, i + 1
            while r < len(s) and l >= 0 and s[r] == s[l]:
                if r - l + 1> resLen:
                    resLen = r - l + 1
                    res = (l, r)
                l -= 1
                r += 1

        l, r = res
        return s[l : r + 1]