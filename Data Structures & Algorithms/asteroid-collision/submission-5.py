class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in range(len(asteroids)):
            if stack and stack[-1] > 0 and asteroids[i] < 0:
                same = False
                while stack and stack[-1] > 0 and asteroids[i] < 0 and stack[-1] <= abs(asteroids[i]):
                    same = stack.pop() == abs(asteroids[i])
                    if same:
                        break
                if not same and (not stack or stack[-1] < 0):
                    stack.append(asteroids[i])
            else:
                stack.append(asteroids[i])
        return stack