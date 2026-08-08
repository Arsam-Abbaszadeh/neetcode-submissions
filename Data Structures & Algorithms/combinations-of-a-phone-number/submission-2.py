class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = ['']
        dig_let = ['abc', 'def', 'ghi', 'jkl', 'mno','pqrs', 'tuv', 'wxyz']
        for i in range(len(digits)):
            temp = []
            for curStr in res:
                for char in dig_let[int(digits[i]) - 2]:
                        temp.append(curStr + char)
            res = temp
        return res




