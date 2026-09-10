class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for level in range(n // 2):
            last = n - 1 - level
            # one edge of this ring, including both corners
            side = n - (level * 2)
            # shift the ring clockwise (side - 1) times => 90 degrees
            for _ in range(side - 1):
                temp = None
                # top row
                for col in range(level, last + 1):
                    matrix[level][col], temp = temp, matrix[level][col]

                # right col (skip the corner already taken from the top)
                for row in range(level + 1, last + 1):
                    matrix[row][last], temp = temp, matrix[row][last]

                # bottom row (skip the corner already taken from the right)
                for col in range(last - 1, level - 1, -1):
                    matrix[last][col], temp = temp, matrix[last][col]

                # left col (skip bottom corner; last write closes back to the start)
                for row in range(last - 1, level - 1, -1):
                    matrix[row][level], temp = temp, matrix[row][level]