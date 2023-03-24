# using trie for update
from copy import deepcopy
from typing import List
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefix_sum = deepcopy(matrix)
        self.len_y, self.len_x = len(matrix), len(matrix[0])
        for y in range(self.len_y):
            for x in range(1, self.len_x):
                self.prefix_sum[y][x] += self.prefix_sum[y][x-1]

    def update(self, row: int, col: int, val: int) -> None:
        prev = self.matrix[row][col]
        self.matrix[row][col] = val
        for c in range(col, self.len_x):
            self.prefix_sum[row][c] += val - prev

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # return prefix_sum[row2][col2] - prefix_sum[row2][col1] - prefix_sum[row1][col2] + prefix_sum[row1][col1]
        _sum = 0
        for r in range(row1, row2 + 1):
            if col1 > 0:
                _sum += self.prefix_sum[r][col2] - self.prefix_sum[r][col1-1]
            else:
                _sum += self.prefix_sum[r][col2]
        return _sum

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
