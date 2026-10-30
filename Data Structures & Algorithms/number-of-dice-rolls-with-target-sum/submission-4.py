class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        lim = 1000000007
        dp = {}
        
        def reach_target(rem_n, rem_target):
            cached = dp.get((rem_n, rem_target), None)
            if cached is not None:
                return cached

            if rem_n == 0:
                if rem_target == 0:
                    return 1
                return 0

            finds = 0
            for roll in range(1, k + 1):
                if rem_target - roll >= 0:
                    finds += reach_target(rem_n - 1, rem_target - roll)
            dp[(rem_n, rem_target)] = finds
            return finds

        count = reach_target(n, target)
        return count % lim
