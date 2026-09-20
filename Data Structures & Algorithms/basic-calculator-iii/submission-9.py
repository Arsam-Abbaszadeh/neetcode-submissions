class Solution:

    def _operateNums(self, operator, num1, num2):
        match operator:
            case '*': return num1 * num2
            case '+': return num1 + num2
            case '/': 
                res = num1 / num2 # may be different
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
        NUM = 'NUM'
        OPERATOR = 'OP'
        BRACKET = 'BRACKET'
        prev = None
        idx = 0

        def isUnaryNeg(other):
            part = prev != NUM and s[idx] == '-'
            if other == NUM:
                rest = idx < len(s) - 1 and s[idx + 1].isnumeric()
            else:
                rest = idx < len(s) - 1 and s[idx + 1] == '('

            return rest and part

        def evalSubEx():
            nonlocal idx
            nonlocal prev
            opStack = deque()
            numStack = deque()

            while idx < len(s):
                if s[idx] == ' ':
                    idx += 1
                elif s[idx].isnumeric() or isUnaryNeg(NUM):
                    end = idx + 1
                    while end < len(s) and s[end].isnumeric():
                        end += 1
                    if isUnaryNeg(NUM):
                        num = -int(s[idx + 1: end])
                    else:
                        num = int(s[idx:end])

                    if opStack and (opStack[-1] == '*' or opStack[-1] == '/'):
                        num = self._operateNums(opStack.pop(), numStack.pop(), num)

                    numStack.append(num)
                    idx = end
                    prev = NUM
                elif s[idx] == '(' or isUnaryNeg(BRACKET):
                    unaryNeg = isUnaryNeg(BRACKET)
                    if unaryNeg:
                        idx += 2
                    else:
                        idx += 1

                    num = evalSubEx()
                    if unaryNeg:
                        num = -num

                    if opStack and (opStack[-1] == '*' or opStack[-1] == '/'):
                        num = self._operateNums(opStack.pop(), numStack.pop(), num)
                    numStack.append(num)
                    prev = NUM

                elif self._isOperator(s[idx]):
                    prev = OPERATOR
                    opStack.append(s[idx])
                    idx += 1

                elif s[idx] == ')':
                    prev = BRACKET
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
