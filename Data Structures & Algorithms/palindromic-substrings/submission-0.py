class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)

        def check(l, r):
            nonlocal count
            while l >= 0 and r < n and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
                
        for i in range(n):
            check(i ,i)
            check(i, i + 1)

        return count
        