import heapq
from collections import defaultdict
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if groupSize == 1 and len(hand) > 0:
            return True

        groups = defaultdict(list)
        hand.sort()
        groups_finished = 0
        for num in hand:
            new_size = -1
            if (num - 1) in groups and len(groups[num - 1]) > 0:
                new_size = heapq.heappop(groups[num - 1]) - 1
                if -new_size == groupSize:
                    groups_finished += 1
                    continue
                    
            heapq.heappush(groups[num], new_size)

        return groups_finished * groupSize == len(hand)

