from collections import deque
class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        m, n = len(maze), len(maze[0]) 
        queue = [[0,"",*ball]]
        visitCheck = {
            (ball[0], ball[1]) : (0,"")
        }
        # print(visitCheck)
        while queue:
            # print(queue)
            distance, instructions, y, x = heapq.heappop(queue)
            if [y,x] == hole:
                return instructions
            for instruction, dy, dx in [('r',0,1),('d',1,0),('l',0,-1),('u',-1,0)]:
                ninstruction, ny, nx, ndistance = instructions + instruction, y, x, distance
                while 0<= ny+dy <m and 0<= nx+dx <n and maze[ny+dy][nx+dx] == 0 and [ny, nx]!= hole:
                    ny+=dy
                    nx+=dx
                    ndistance+=1
                if (ny,nx) not in visitCheck or visitCheck[(ny,nx)] > (ndistance, instructions):
                    visitCheck[(ny,nx)] = (ndistance, instructions)
                    heapq.heappush(queue,[ndistance, instructions + instruction, ny, nx])
        return "impossible"


        