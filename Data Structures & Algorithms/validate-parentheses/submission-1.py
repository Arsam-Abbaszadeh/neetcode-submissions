class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            ')' : '(',
            '}' : '{',
            ']': '['
        }

        stack = []
        for char in s:
            if stack and stack[-1] == mapping.get(char):
                stack.pop()
            else:
                stack.append(char)

        return len(stack) == 0