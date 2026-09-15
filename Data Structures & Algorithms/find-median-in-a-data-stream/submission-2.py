class MedianFinder:
    def __init__(self):
        self.smallerMaxHeap  = []
        self.largerMinHeap = []

    def addNum(self, num: int) -> None:
        #  which heap to add this to
        #  every value in smaller heap is smaller than larger heap
        #  abs(smaller - larger) = 1 or 0
        if not self.largerMinHeap and not self.smallerMaxHeap:
            self.largerMinHeap.append(num)
            return

        elif not self.smallerMaxHeap and self.largerMinHeap:
            if self.largerMinHeap[0] >= num:
                self.smallerMaxHeap.append(-num)
            else:
                self.smallerMaxHeap = [-self.largerMinHeap[0]]
                self.largerMinHeap = [num]

        elif num > self.largerMinHeap[0]:
            heapq.heappush(self.largerMinHeap, num)
            if len(self.largerMinHeap) - len(self.smallerMaxHeap) == 2:
                movingVal = heapq.heappop(self.largerMinHeap)
                heapq.heappush(self.smallerMaxHeap, -movingVal)
        
        elif num < -self.smallerMaxHeap[0]:
            heapq.heappush(self.smallerMaxHeap, -num)
            if len(self.smallerMaxHeap) - len(self.largerMinHeap) == 2:
                movingVal = heapq.heappop(self.smallerMaxHeap)
                heapq.heappush(self.largerMinHeap, -movingVal)

        # val can go in either, put in whichever has smaller length
        elif len(self.smallerMaxHeap) < len(self.largerMinHeap):
            heapq.heappush(self.smallerMaxHeap, -num)
        else:
            heapq.heappush(self.largerMinHeap, num)
        

    def findMedian(self) -> float:
        if len(self.largerMinHeap) > len(self.smallerMaxHeap):
            return self.largerMinHeap[0]
        
        if len(self.largerMinHeap) < len(self.smallerMaxHeap):
            return -self.smallerMaxHeap[0]

        return (self.largerMinHeap[0] - self.smallerMaxHeap[0]) / 2



