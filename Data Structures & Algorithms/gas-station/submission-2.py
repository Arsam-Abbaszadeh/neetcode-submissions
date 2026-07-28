class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        candidates = []
        for i in range(len(gas)):
            candidates.append((gas[i], cost[i], i))
        candidates.sort(reverse=True, key= lambda x: x[0] - x[1])

        for g, c, i in candidates:
            if g - c < 0:
                break
            tank = 0
            gas_station = i
            
            while True:
                tank += gas[gas_station] - cost[gas_station]
                gas_station += 1
                gas_station = gas_station % len(candidates)

                if tank <= 0 or gas_station == i:
                    break

            if tank >= 0 and gas_station == i:
                return i
        return -1
                
            
