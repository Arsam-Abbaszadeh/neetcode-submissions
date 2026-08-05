import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # k log n, heapify first and then remove k nodes in log n time
        minheap = []
        for x, y in points:
            dist = x **2  + y ** 2
            minheap.append((dist, x, y))

        heapq.heapify(minheap)
        res = []
        for _ in range(k):
            _, x, y = heapq.heappop(minheap)
            res.append(([x, y]))
        return res
