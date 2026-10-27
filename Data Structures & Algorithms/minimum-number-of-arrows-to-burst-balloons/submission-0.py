class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key= lambda x: x[0])
        groups = 1
        last_start = points[0][1]

        for start, end in points[1:]:
            if start > last_start:
                groups += 1
                last_start = end
            else:
                if end < last_start:
                    last_start = end
        
        return groups
