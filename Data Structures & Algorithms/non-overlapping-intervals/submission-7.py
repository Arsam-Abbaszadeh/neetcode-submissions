class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prev = 0
        res = 0

        for i in range(1, len(intervals)):
            c_s, c_e  = intervals[i]
            _, p_e = intervals[prev]
            if p_e <= c_s:
                prev = i # or append the interval
                continue
                
            if p_e >= c_e:
                prev = i
            res += 1

        return res