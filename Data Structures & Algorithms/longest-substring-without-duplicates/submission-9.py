class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # more concise code after seen solutions
        longest = 0
        seen = {}
        start = 0
        for i, char in enumerate(s):
            if char in seen:
                start = max(seen[char] + 1, start)
            seen[char] = i
            longest = max(i - start + 1, longest)
        
        return longest