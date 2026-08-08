class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(curr, opening, closing):
            if opening == 0 and closing == 0:
                res.append(''.join(curr))

            if opening > 0:
                curr.append('(')
                dfs(curr, opening - 1, closing)
                curr.pop()

            if closing > 0 and closing > opening:
                curr.append(')')
                dfs(curr, opening, closing - 1)
                curr.pop()

        dfs([], n, n)
        return res