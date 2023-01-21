# https://leetcode.com/problems/maximum-number-of-visible-points/
# 1 <= points.length <= 105
# points[i].length == 2
# location.length == 2
# 0 <= angle < 360
# 0 <= posx, posy, xi, yi <= 100

class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int: