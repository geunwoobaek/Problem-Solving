# https://leetcode.com/problems/the-skyline-problem/
# Input: buildings = [[0,2,3],[2,5,3]]
# Output: [[0,3],[5,0]]
# Input: buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
# # Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
# 1 <= buildings.length <= 104
# 0 <= lefti < righti <= 231 - 1
# 1 <= heighti <= 231 - 1
# buildings is sorted by lefti in non-decreasing order.

# Approach
# MAX_POINT = 현재까지 읽은 지점의 최대 높이를 가지고 있는 X,Y 좌표
# 1. NEW_POINT(새롭게 읽는 점)
# - NEW_POINT의 LEFT가 MAX_POINT의 RIGHT보다 크면 HEAP에서 하나씩 뺀다.
#   이때 뺀점의 RIGHT가 현재 MAX_POINT의 RIGHT보다 크면 MAX_POINT를 갱신한다.
# - NEW_POINT의 HEIGHT가 MAX_POINT보다 크면 MAX_POINT를 갱신한다.
# 2. HEAP에 넣는다.
# SweepLine 알고리즘을 사용한다.
import heapq
from typing import List


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        positions = sorted(list(set([x for building in buildings for x in building[:2]])))
        max_point= [0,0] # x, y
        result = []
        heap = [] # [-y, idx]
        buildings.sort(key=lambda x: [x[0],-x[2]])
        for idx, building in enumerate(buildings):
            left, _, height = building
            while heap and buildings[heap[0][1]][1] < left:
                _, curr_idx = heapq.heappop(heap)
                while heap and buildings[heap[0][1]][1] <= buildings[curr_idx][1]:
                    heapq.heappop(heap)
                next_height = buildings[heap[0][1]][2] if heap else 0
                if max_point[1] != next_height:
                    max_point = [buildings[curr_idx][1], next_height]
                    result.append(max_point)
            if height > max_point[1]:
                max_point = [left, height]
                result.append(max_point)
            heapq.heappush(heap, [-height, idx])
        while heap:
            _, curr_idx = heapq.heappop(heap)
            while heap and buildings[heap[0][1]][1] <= buildings[curr_idx][1]:
                heapq.heappop(heap)
            next_height = buildings[heap[0][1]][2] if heap else 0
            if max_point[1] != next_height:
                max_point = [buildings[curr_idx][1], next_height]
                result.append(max_point)

        return result  

class BruteForceclassSolution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # Collect and sort the unique positions of all the edges.
        positions = sorted(list(set([x for building in buildings for x in building[:2]])))
        
        # 'answer' for skyline key points
        answer = []
        
        # For each position, draw an imaginary vertical line.
        for position in positions:
            # current max height.
            max_height = 0
            
            # Iterate over all the buildings:
            for left, right, height in buildings:
                # Update 'max_height' if necessary.
                if left <= position < right:
                    max_height = max(max_height, height)
            
            # If its the first key point or the height changes, 
            # we add [position, max_height] to 'answer'.
            if not answer or max_height != answer[-1][1]:
                answer.append([position, max_height])
                
        # Return 'answer' as the skyline.
        return answer




print(Solution().getSkyline([[1,2,1],[1,2,2],[1,2,3]]) == [[1,3],[2,0]])
print(Solution().getSkyline([[0,2,3],[2,5,3]]) ==   [[0,3],[5,0]])
print(Solution().getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]) == [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]])

