class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        def dfs(opening, closing):
            if opening == closing == 0:
                res.append(''.join(stack))

            if opening > 0:
                stack.append('(')
                dfs(opening - 1, closing)
                stack.pop()

            if closing > 0 and closing > opening:
                stack.append(')')
                dfs(opening, closing - 1)
                stack.pop()

        dfs(n, n)
        return res