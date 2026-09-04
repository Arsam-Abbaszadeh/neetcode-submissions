class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
         # greedy check if limit is possible
        def validLimit(limit) -> bool:
            day = 1
            p = 0
            while day <= days and p < len(weights) and weights[p] <= limit:
                loaded = 0
                while p < len(weights) and loaded + weights[p] <= limit:
                    loaded += weights[p]
                    p += 1
                day += 1
                
            return day - 1 <= days and p == len(weights)
            
        # find max upper limit
        l = math.ceil(sum(weights) / days)
        packagesPerDay = math.ceil(len(weights) / days)
        total = 0
        i = 0
        while i < packagesPerDay:
            total += weights[i]
            i += 1
        r = max(total, l)
        for j in range(i, len(weights)):
            total += weights[j] - weights[j - packagesPerDay]
            r = max(total, r)
        prev = -1

        while l <= r:
            mid = (l + r) // 2
            if validLimit(mid):
                prev = mid
                r = mid - 1
            else:
                l = mid + 1

        return prev


       