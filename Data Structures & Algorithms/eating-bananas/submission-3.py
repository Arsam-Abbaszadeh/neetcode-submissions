class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def calc_time(k):
            time = 0
            for p in piles:
                time += math.ceil(p / k)
            return time

        end = max(piles)
        start = 1
        prev = 0
        while start <= end:
            mid = (start + end) // 2
            time = calc_time(mid)
            if time <= h:
                prev = mid
                end = mid - 1
            else:
                start = mid + 1
        return prev