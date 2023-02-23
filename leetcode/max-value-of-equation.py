# solve using monolgue heap
# (-(y - x),i)
import heapq
import math


class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        hq = []
        res = -math.inf
        for i, point in enumerate(points):
            while hq and point[0] - points[hq[0][1]][0] > k:
                heapq.heappop(hq)
            if hq:
                res = max(res, point[0] - points[hq[0][1]]
                          [0] + point[1] + points[hq[0][1]][1])
            heapq.heappush(hq, [-(point[1] - point[0]), i])
        return res
