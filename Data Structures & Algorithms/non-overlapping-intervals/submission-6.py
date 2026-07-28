class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        final = [0]

        for i in range(1, len(intervals)):
            c_s, c_e  = intervals[i]
            _, p_e = intervals[final[-1]]
            if p_e <= c_s:
                final.append(i) # or append the interval
            
            if p_e >= c_e:
                final.pop()
                final.append(i)

        return len(intervals) - len(final)