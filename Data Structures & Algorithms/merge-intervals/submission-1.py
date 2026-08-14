class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res, n = [], len(intervals)
        intervals.sort(key=lambda x: x[0])
        res.append(intervals[0])
        for i in range (1, n):
            prev = res[-1]
            curr = intervals[i]
            if prev[0] == curr[0] or curr[0] <= prev[1]:
                res[-1][0] = min(prev[0], curr[0])
                res[-1][1] = max(prev[1], curr[1])
            else:
                res.append(curr)


        return res
