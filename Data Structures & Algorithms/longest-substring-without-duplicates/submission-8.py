class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        curr = 0
        seen = {}
        start = 0
        for i, char in enumerate(s):
            if char in seen and seen[char] >= start:
                longest = max(curr, longest)
                curr -= (seen[char] - start + 1)
                start = seen[char] + 1
            curr += 1
            seen[char] = i
        
        return max(longest, curr)