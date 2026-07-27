from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        for token in tokens:
            match token:
                case '+':
                    cur = stack.pop()
                    cur2 = stack.pop()
                    newVal = cur + cur2
                    stack.append(newVal)
                case '-':
                    cur = stack.pop()
                    cur2 = stack.pop()
                    newVal = cur2 - cur
                    stack.append(newVal)
                case '/':
                    cur = stack.pop()
                    cur2 = stack.pop()
                    newVal = int(cur2 / cur)
                    stack.append(newVal)
                case '*':
                    cur = stack.pop()
                    cur2 = stack.pop()
                    newVal = cur2 * cur
                    stack.append(newVal)
                case _:
                    stack.append(int(token))
        
        return stack.pop()