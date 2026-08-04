import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        nums.sort(reverse=True)
        self.topK = nums[:k]
        heapq.heapify(self.topK)
        self.k = k

    def add(self, val: int) -> int:
        if len(self.topK) < self.k:
            heapq.heappush(self.topK, val)
        elif self.topK[0] < val:
            heapq.heappush(self.topK, val)
            heapq.heappop(self.topK)
        
        return self.topK[0]
        
