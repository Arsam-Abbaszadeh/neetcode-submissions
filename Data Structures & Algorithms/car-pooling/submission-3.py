import heapq
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        nextCapChange = []
        for change, start, end in trips:
            nextCapChange.append((start, change))
            nextCapChange.append((end, -change))
        
        # heapq.heapify(nextCapChange)
        nextCapChange.sort()
        curCap = 0
        for _ in range(len(nextCapChange)):
            _, change = heapq.heappop(nextCapChange)
            curCap += change
            if curCap > capacity:
                return False

        return True
