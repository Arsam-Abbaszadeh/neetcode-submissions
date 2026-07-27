class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for pos, spd in zip(position, speed):
            cars.append((pos, spd))
        cars.sort(reverse=True, key = lambda x: x[0])

        stack = []
        for pos, spd in cars:
            time = (target - pos) / spd
            if stack and stack[-1] >= time:
                continue
            stack.append(time)

        return len(stack)



