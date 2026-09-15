class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        banned = set()
        n = len(senate)

        while True:
            for sidx in range(n):
                # This senator may have been banned earlier
                if sidx in banned:
                    continue

                currentParty = senate[sidx]
                bannedSomeone = False

                # Search chronologically after this senator,
                # wrapping around when we reach the end.
                for offset in range(1, n):
                    j = (sidx + offset) % n

                    if j in banned:
                        continue

                    if senate[j] != currentParty:
                        banned.add(j)
                        bannedSomeone = True
                        break

                # Couldn't find a living opponent anywhere
                if not bannedSomeone:
                    return "Radiant" if currentParty == 'R' else "Dire"