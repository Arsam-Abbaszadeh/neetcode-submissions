import heapq
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        nextCapChange = []
        for change, start, end in trips:
            heapq.heappush(nextCapChange, (start, change))
            heapq.heappush(nextCapChange, (end, -change))
        
        curCap = 0
        for _ in range(len(nextCapChange)):
            _, change = heapq.heappop(nextCapChange)
            curCap += change
            if curCap > capacity:
                return False

        return True
