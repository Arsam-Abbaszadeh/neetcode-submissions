class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        target = sum(matchsticks) / 4
        if target != (target // 1) or len(matchsticks) < 4:
            return False

        sides = [0] * 4
        matchsticks.sort(reverse=True)
        def backtrack(i):
            if i == len(matchsticks):
                return True
            
            for j in range(4):
                if sides[j] + matchsticks[i] <= target:
                    sides[j] += matchsticks[i]
                    if backtrack(i + 1):
                        return True
                    sides[j] -= matchsticks[i]
            return False
        return backtrack(0)
