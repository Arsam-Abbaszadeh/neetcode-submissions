class Solution:
    def checkValidString(self, s: str) -> bool:
        leftmin = leftmax = 0
        for c in s:
            if c == '(':
                leftmin += 1
                leftmax += 1
            elif c == ')':
                leftmin = max(0, leftmin - 1)
                leftmax -= 1
                if leftmax < 0:
                    return False
            else:
                leftmax += 1
                leftmin = max(0, leftmin - 1)

        return leftmin == 0