from typing import List

## find rightmost, leftmost, topmost, bottommost
## dfsSolution = O(n^2) 이분탐색을 이용하면 O(nlogn)이 될 수 있음
class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        ## find rightmost
        def find_rightmost(y):
            left, right = y, len(image[0])
            while left < right:
                mid = (left + right) // 2
                if any(image[i][mid] == '1' for i in range(len(image))):
                    left = mid + 1
                else:
                    right = mid
            return left - 1
        ## find leftmost
        def find_leftmost(y):
            left, right = 0, y
            while left < right:
                mid = (left + right) // 2
                if any(image[i][mid] == '1' for i in range(len(image))):
                    right = mid
                else:
                    left = mid + 1
            return left
        def find_topmost(x):
            left, right = 0, x
            while left < right:
                mid = (left + right) // 2
                if any(image[mid][j] == '1' for j in range(len(image[0]))):
                    right = mid
                else:
                    left = mid + 1
            return left
        def find_bottommost(x):
            left, right = x, len(image)
            while left < right:
                mid = (left + right) // 2
                if any(image[mid][j] == '1' for j in range(len(image[0]))):
                    left = mid + 1
                else:
                    right = mid
            return left - 1

        ## get rightmost, leftmost, topmost, bottommost
        return (find_rightmost(y) - find_leftmost(y) + 1) * (find_bottommost(x) - find_topmost(x) + 1)
