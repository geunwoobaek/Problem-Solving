# https://leetcode.com/problems/maximal-rectangle/

# Constraints
# rows == matrix.length
# cols == matrix[i].length
# 1 <= row, cols <= 200
# matrix[i][j] is '0' or '1'.

# 로직
# 	1.  해당 포인트가 시작점인 가로를 포함하는 사각형을 계산 한다.
# 	- 먼저 가로를 계산하고, 해당 지점의 바로 밑에서 가로를 계산한다.
# 	2. 해당 포인트 지점의 모든계산이 마치면 다음 지점으로 이동한다.
# 가로길이에 대해서 먼저 cache한다.

from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        result = 0
        cache_matrix = matrix
        def allocate_cache_matrix(y, x):
            if x == len(matrix[0]) or matrix[y][x] == '0':
                return 0
            else:
                cache_matrix[y][x] = 1 + allocate_cache_matrix(y, x+1)
                return cache_matrix[y][x]

        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                if cache_matrix[y][x] == '1':
                    cache_matrix[y][x] = allocate_cache_matrix(y, x)
        # 로직
        # 	1.  해당 포인트가 시작점인 가로를 포함하는 사각형을 계산 한다.
        # 	- 먼저 가로를 계산하고, 해당 지점의 바로 밑에서 가로를 계산한다.
        # 	2. 해당 포인트 지점의 모든계산이 마치면 다음 지점으로 이동한다.
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                if cache_matrix[y][x] == '0':
                    continue
                curr_row = cache_matrix[y][x]
                curr_y = y
                while curr_y < len(matrix) and cache_matrix[curr_y][x]!= '0':
                    curr_row = min(curr_row, cache_matrix[curr_y][x])
                    curr_sum = (curr_y - y + 1) * curr_row
                    result = max(curr_sum, result)
                    curr_y +=1
        return result



Smatrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(Solution().maximalRectangle(Smatrix))