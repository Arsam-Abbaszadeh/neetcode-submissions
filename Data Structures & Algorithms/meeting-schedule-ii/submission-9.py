from _heapq import heappop
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

from heapq import heappush, heapify, heapreplace

class Inter_wrapper:
    def __init__(self, interval: Interval) -> None:
        self.interval = interval

    def __lt__(self, other: Inter_wrapper) :
        return self.interval.end < other.interval.end

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # use a min heap to acheive nlogn instead n^2
        if not intervals:
            return 0
        sorted_itv = sorted(intervals, key = lambda x: x.start)
        rooms = [Inter_wrapper(sorted_itv[0])]
        heapify(rooms)

        for i in range(1, len(sorted_itv)):
            itv = Inter_wrapper(sorted_itv[i])
            if rooms[0].interval.end <= itv.interval.start:
                heappop(rooms)
            heappush(rooms, itv)

        return len(rooms)