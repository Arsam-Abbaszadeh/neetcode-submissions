class Solution:
    def isPalindrome(self, s: str) -> bool:
        end = len(s) - 1
        start = 0

        while start < end:
            while not s[end].isalnum() and end >= 0:
                end -= 1
            while not s[start].isalnum() and start < len(s) - 1:
                start += 1
            
            if s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1
        
        return True