class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort(key = lambda slot: slot[0])
        slots2.sort(key = lambda slot: slot[0])
        p1, p2 = 0, 0

        while p1 < len(slots1) and p2 < len(slots2):
            start1, end1 = slots1[p1]
            start2, end2 = slots2[p2]

            start_overlap = max(start1, start2)
            end_overlap = min(end1, end2)

            if end_overlap - start_overlap >= duration:
                return [start_overlap, start_overlap + duration]
            
            if end1 > end2:
                p2 += 1
            else:
                p1 += 1
                
        return []

            
            
            