class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        self.matrix = matrix
        row, col = len(matrix), len(matrix[0])
        self.sum = self.matrix
        for x in range(row):
            for y in range(col):
                if x == 0 and y == 0:
                    self.matrix[x][y] += 0
                elif x == 0 and y >= 1:
                    self.matrix[0][y] += self.matrix[0][y - 1]
                elif y == 0 and x >= 1:
                    self.matrix[x][0] += self.matrix[x - 1][0]
                else:
                    self.matrix[x][y] += self.matrix[x - 1][y] + self.matrix[x][y - 1] - self.matrix[x - 1][y - 1]
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        print(self.matrix)
        if len(self.matrix) == 1 and not col1:
            return self.matrix[0][col2]
        elif not row1 + col1:
            return self.matrix[row2][col2]
        elif col1 and len(self.matrix) == 1:
            return self.matrix[0][col2] - self.matrix[0][col1 - 1]
        elif not len(self.matrix):
            return 0
        elif len(self.matrix[0]) == 1 and not row1:
            return self.matrix[row2][0]
        elif row1 and len(self.matrix[0]) == 1:
            return self.matrix[row2][0] - self.matrix[row1 - 1][0]
        elif 0 not in [row1, col1,col2,row2]:
            return self.matrix[row2][col2] - self.matrix[row1 - 1][col2] - self.matrix[row2][col1 - 1] + self.matrix[row1  - 1][col1 - 1]
        elif not row1 + row2 and col1:
            return self.matrix[0][col2] - self.matrix[0][col1 - 1]
        elif not col1 + col2 and row1:
            return self.matrix[row2][0] - self.matrix[row1 - 1][0]
        elif not row1:
            return self.matrix[row2][col2] - self.matrix[row2][col1 - 1]
        elif not col1:
            return self.matrix[row2][col2] - self.matrix[row1 - 1][col2]
