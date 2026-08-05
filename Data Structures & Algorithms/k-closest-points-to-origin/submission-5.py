class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxheap = []
        for x, y in points:
            dist = x ** 2 + y ** 2
            if len(maxheap) < k:
                heapq.heappush(maxheap, (-dist, x, y))
            elif maxheap[0][0] < -dist:
                heapq.heappop(maxheap)
                heapq.heappush(maxheap, (-dist, x, y))
        
        return list(map(lambda point: [point[1], point[2]], maxheap))