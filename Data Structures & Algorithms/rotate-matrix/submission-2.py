class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for layer in range(n // 2):
            first = layer
            last = n - 1 - layer

            for i in range(first, last):
                temp = None
                # top side
                matrix[first][i], temp = temp, matrix[first][i]

                # right side
                matrix[i][last], temp = temp, matrix[i][last]

                # bottom side
                matrix[last][n - i - 1], temp = temp, matrix[last][n - i - 1]

                # left side
                matrix[n - i - 1][first], temp =  temp, matrix[n - i - 1][first]

                # replace top with left side value
                matrix[first][i], temp = temp, matrix[first][i]




