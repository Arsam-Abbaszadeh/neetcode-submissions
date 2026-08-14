class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        count = Counter(hand)
        hand.sort()
        for num in hand:
            if count[num]:
                count[num] -= 1
                for i in range(num + 1, num + groupSize):
                    if not count[i]:
                        return False
                    count[i] -= 1

        return True