class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # bottom up approach not space optimized
        L = len(strs)
        # memo = [defaultdict(int) for _ in range(L + 1)]
        # memo = defaultdict(int)
        memo = {}
        # memo[0][0] = 0

        def mnCount(s: str) -> tuple[int, int]:
            m = n = 0
            for c in s:
                if c == '0':
                    m += 1
                else:
                    n += 1
            return m, n

        largestSub = 0
        memo[(0, 0)] = 0
        for s in strs:
            new_memo = memo.copy()
            for (tm, tn), subC in memo.items():
                cm, cn = mnCount(s)
                if tm + cm <= m and tn + cn <= n:
                    oldVal = new_memo.get((tm + cm, tn + cn), 0)
                    new_memo[(tm + cm, tn + cn)] = max(oldVal, subC + 1)
                    largestSub = max(largestSub, subC + 1, oldVal)
            memo = new_memo
            
        return largestSub



