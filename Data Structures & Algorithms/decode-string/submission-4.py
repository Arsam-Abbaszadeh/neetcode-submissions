class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
            else:
                temp_stack = []
                while stack[-1] != '[':
                    temp_stack.append(stack.pop())
                curr_str = ''.join(reversed(temp_stack))
                stack.pop()

                temp_stack = []
                while stack and stack[-1].isdigit():
                    temp_stack.append(stack.pop())

                copy_count = int(''.join(reversed(temp_stack)))
                stack.append(curr_str * copy_count)

        return ''.join(stack)




