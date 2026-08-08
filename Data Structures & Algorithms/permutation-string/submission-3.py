class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        subSc = Counter(s1)
        subl = len(s1)
        subSc2 = Counter(s2[0: subl])

        for i in range(len(s2) - subl + 1):
            if i > 0:
                subSc2[s2[i - 1]] -= 1
                idx = i + subl - 1 if subl < len(s2) else -1
                subSc2[s2[idx]] += 1

            same = True
            for key in subSc.keys():
                if subSc2[key] != subSc[key]:
                    same = False
                    break
            if same:
                return True
        return False



