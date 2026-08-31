class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        curr = asteroids
        new = []

        while len(curr) >= 2:
            skip = 0
            collision = False
            for i in range(len(curr)):
                if i + skip >= len(curr) - 1:
                    if i + skip == len(curr) - 1:
                        new.append(curr[i + skip])
                    break

                if curr[i + skip] > 0 and curr[i + skip + 1] < 0:
                    collision = True
                    res = curr[i + skip] + curr[i + skip + 1]
                    if res > 0:
                        new.append(curr[i + skip])
                    elif res < 0:
                        new.append(curr[i + skip + 1])
                    skip += 1
                else:
                    new.append(curr[i + skip])
            curr = new
            new = []
            if not collision:
                break

        return curr