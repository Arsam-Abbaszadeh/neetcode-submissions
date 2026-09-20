class Solution:

    def _operateNums(self, operator, num1, num2):
        match operator:
            case '*': return num1 * num2
            case '+': return num1 + num2
            case '/' : 
                res = num1 / num2
                if res > 0:
                    return res // 1
                else:
                    return int(math.ceil(res))
                
                
            case '-' : return num1 - num2

    def _isOperator(self, operator):
        return (
            operator == '*'
            or operator == '/'
            or operator == '+'
            or operator == '-'
        )

    def calculate(self, s: str) -> int:

        idx = 0
        def evalSubEx():
            nonlocal idx
            opStack = deque()
            numStack = deque()
            # prev = None

            while idx < len(s):
                if s[idx].isnumeric():
                    end = idx + 1
                    while end < len(s) and s[end].isnumeric():
                        end += 1
                    num = int(s[idx : end])
                    if opStack and (opStack[-1] == '*' or opStack[-1] == '/'):
                        num = self._operateNums(opStack.pop(), numStack.pop(), num)

                    numStack.append(num)
                    idx = end
                elif self._isOperator(s[idx]):
                    opStack.append(s[idx])
                    idx += 1
                elif s[idx] == '(':
                    idx += 1
                    num = evalSubEx()
                    if opStack and (opStack[-1] == '*' or opStack[-1] == '/'):
                        num = self._operateNums(opStack.pop(), numStack.pop(), num)
                    numStack.append(num)
                elif s[idx] == ')':
                    idx += 1
                    break
            
            while opStack:
                num1 = numStack.popleft()
                num2 = numStack.popleft()
                res = self._operateNums(
                    opStack.popleft(),
                    num1,
                    num2
                )
                numStack.appendleft(res)
            
            return numStack[0]

        return int(evalSubEx())
