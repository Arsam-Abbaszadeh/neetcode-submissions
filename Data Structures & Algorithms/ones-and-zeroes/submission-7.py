class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # bottom up approach space optimized
        memo = {}
        largestSub = 0
        memo[(0, 0)] = 0
        for s in strs:
            new_memo = memo.copy()
            cm = s.count('0')
            cn = len(s) - cm
            for (tm, tn), subC in memo.items():
                if tm + cm <= m and tn + cn <= n:
                    oldVal = new_memo.get((tm + cm, tn + cn), 0)
                    new_memo[(tm + cm, tn + cn)] = max(oldVal, subC + 1)
                    largestSub = max(largestSub, subC + 1, oldVal)
            memo = new_memo
            
        return largestSub