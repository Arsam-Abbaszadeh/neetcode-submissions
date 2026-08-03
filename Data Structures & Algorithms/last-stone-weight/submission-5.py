class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        heap = [-x for x in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            m1 = heapq.heappop(heap)
            m2 = heapq.heappop(heap)
            diff = m1 - m2
            if abs(diff) > 0:
                heapq.heappush(heap, diff)

        return abs(heap[0]) if len(heap) else 0
