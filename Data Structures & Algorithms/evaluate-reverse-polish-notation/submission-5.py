class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack  = []

        def do_operation(num1, num2, op):
            match op:
                case '+':
                    return num1 + num2
                case '-':
                    return num1 - num2
                case '/':
                    return int(num1 / num2)
                case '*':
                    return num1 * num2

        for token in tokens:
            if token not in {"+", "-", "*", "/"}:
                num_stack.append(int(token))
            else:
                num2 = num_stack.pop()
                num1 = num_stack.pop()
                calc = do_operation(num1, num2, token)
                num_stack.append(calc)
        
        return num_stack[0] 
            
        
            