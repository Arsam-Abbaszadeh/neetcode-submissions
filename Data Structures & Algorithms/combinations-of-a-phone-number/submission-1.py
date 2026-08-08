class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if digits:
            dig_let = ['abc', 'def', 'ghi', 'jkl', 'mno','pqrs', 'tuv', 'wxyz']
            stack = []
            def backtrack(i):
                if i == len(digits):
                    res.append(''.join(stack))
                    return
                
                for char in dig_let[int(digits[i]) - 2]:
                    stack.append(char)
                    backtrack(i + 1)
                    stack.pop()
            backtrack(0)        
        return res