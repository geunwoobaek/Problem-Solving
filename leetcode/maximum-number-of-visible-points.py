# https://leetcode.com/problems/maximum-number-of-visible-points/
# 11:44 ~
# 1 <= points.length <= 105
# points[i].length == 2
# location.length == 2
# 0 <= angle < 360
# 0 <= posx, posy, xi, yi <= 100
# locaion, points[i]를 잇는 직선과, y = posy, 사이의 각도를 구합니다.
# 점들을 각도에 따라 정렬합니다.
# 각도가 0~angle인 점들부터 시작해서, 360~angle까지 점들을 찾습니다.
# 각도법이 아니라 호도법을 사용해야합니다.
from collections import deque
from typing import List
import math


class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:

        arr, extra = [], 0
        xx, yy = location

        for x, y in points:
            if x == xx and y == yy:
                extra += 1
                continue
            arr.append(math.atan2(y - yy, x - xx))

        arr.sort()
        arr = arr + [x + 2.0 * math.pi for x in arr]
        angle = math.pi * angle / 180

        l = ans = 0
        for r in range(len(arr)):
            while arr[r] - arr[l] > angle:
                l += 1
            ans = max(ans, r - l + 1)

        return ans + extra
print(Solution().visiblePoints([[1, 1], [2, 2], [3, 3]], 90, [1, 1]) == 3)
