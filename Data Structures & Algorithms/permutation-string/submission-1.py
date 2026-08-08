class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        subSc = Counter(s1)

        subl = len(s1)
        for i in range(len(s2) - subl + 1):
            subSc2 = Counter(s2[i: i + subl])
            same = True
            print(s2[i: i + subl])
            for key in subSc.keys():
                count = subSc2.get(key, 0)
                if count != subSc[key]:
                    same = False
                    break
            if same:
                return True
        return False



