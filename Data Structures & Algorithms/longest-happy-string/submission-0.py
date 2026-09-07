class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = []
        budget = [a, b, c]
        for _ in range(2):
            maxI = -1
            maxA = 0
            for i in range(3):
                if budget[i] > 0 and budget[i] > maxA:
                    maxA = budget[i]
                    maxI = i

            if maxI == -1:
                break
            
            budget[maxI] -= 1
            res.append(self.getChar(maxI))

        i = 1
        while any(budget):
            maxI = -1
            maxA = 0
            for j in range(3):
                char = self.getChar(j)
                if res[i] == char and res[i - 1] == char:
                    continue
                
                if budget[j] > maxA:
                    maxI = j
                    maxA = budget[j]
            
            if maxI == -1:
                break
            budget[maxI] -= 1
            res.append(self.getChar(maxI))
            i += 1

        return ''.join(res)
            
    
    def getChar(self, i):
        if i == 0:
            return 'a'
        elif i == 1:
            return 'b'
        else:
            return 'c'