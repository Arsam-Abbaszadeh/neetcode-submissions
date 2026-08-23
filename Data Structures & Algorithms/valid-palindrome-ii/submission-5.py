class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, left2 = 0, 0
        right, right2 = len(s) - 1, len(s) - 1
        skipped = False
        while left < right:
            if s[left] != s[right]:
                if skipped:
                    break
                skipped = True
                left2 = left
                right2 = right - 1
                right += 1
            left += 1
            right -= 1


        if left >= right:
            print('yo')
            return True

        while left2 < right2:
            if s[left2] != s[right2]:
                return False
            left2 += 1
            right2 -= 1
        return True

