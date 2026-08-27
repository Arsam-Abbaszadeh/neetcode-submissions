class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        total = 0
        for op in operations:
            if op == 'D':
                total += stack[-1] * 2
                stack.append(stack[-1] * 2)
            elif op == 'C':
                val = stack.pop()
                total -= val
            elif op == '+':
                total += stack[-1] + stack[-2]
                stack.append(stack[-1] + stack[-2])
            else:
                total += int(op)
                stack.append(int(op))
        return total
            