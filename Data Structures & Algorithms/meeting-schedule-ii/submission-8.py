"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        sort_itv = sorted(intervals, key = lambda x: x.start)
        rooms = [sort_itv[0]]
        for i in range(1, len(intervals)):
            added = False
            for j in range(len(rooms)):
                if rooms[j].end <= sort_itv[i].start:
                    rooms[j] = sort_itv[i]
                    added = True
                    break
            if not added:
                rooms.append(sort_itv[i])

        return len(rooms)