class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort(key = lambda slot: slot[0])
        slots2.sort(key = lambda slot: slot[0])
        p1, p2 = 0, 0

        while p1 < len(slots1) and p2 < len(slots2):
            # check if allows for duration
            start1, end1 = slots1[p1]
            # if end1 - start1 < duration:
            #     p1 += 1
            #     continue
            start2, end2 = slots2[p2]
            # if end2 - start2 < duration:
            #     p2 += 1
            #     continue

            # check for overlapping time region and adjust accordingly
            start_overlap = max(start1, start2)
            end_overlap = min(end1, end2)
            if end_overlap - start_overlap >= duration:
                return [start_overlap, start_overlap + duration]
            
            # move relevant pointer
            if end1 > end2:
                p2 += 1
            else:
                p1 += 1
        return []

            
            
            