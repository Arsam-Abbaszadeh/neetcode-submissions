import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-x for x in nums]
        heapq.heapify(nums)
        curr = None
        for _ in range(k):
            curr = heapq.heappop(nums)
        return -curr