class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        if len(s) > 12:
            return res
        curr = []

        def backtrack(idx, startIdx):
            if idx == len(s) - 1:
                num = s[startIdx: idx + 1]
                if int(num) <= 255 and len(curr) == 3:
                    curr.append(num)
                    validAdress = '.'.join(curr)
                    res.append(validAdress)
                    curr.pop()
                return
            
            num = s[startIdx: idx + 1]
            if len(curr) == 4 or int(num) > 255:
                return

            currLen = len(res)
            if num != '0':
                backtrack(idx + 1, startIdx)
            
            # basic pruning
            if not (len(curr) == 3 and len(res) > currLen):
                curr.append(num)
                backtrack(idx + 1, idx + 1)
                curr.pop()

        backtrack(0, 0)
        return res
