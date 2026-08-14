class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        found = [0] * 3


        for i in range(len(triplets)):
            flag = False
            for j in range(3):
                if triplets[i][j] > target[j]:
                    flag = True
                    break
            if flag:
                continue
            found = [max(triplets[i][0], found[0]),max(triplets[i][1], found[1]), max(triplets[i][2], found[2])]
        
        return found == target