class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [0]
        for i in range(1, len(temperatures)):
            if stack:
                if temperatures[i] > temperatures[stack[-1]]:
                    while stack and temperatures[i] > temperatures[stack[-1]]:
                        curr = stack.pop()
                        res[curr] = i - curr
            
            stack.append(i)
        return res