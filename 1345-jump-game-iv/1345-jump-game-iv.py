# from collections import deque, defaultdict
# from typing import List


# class Solution:
#     def minJumps(self, arr: List[int]) -> int:
#         n = len(arr)
#         if n == 1:
#             return 0

#         index_list_by_num = defaultdict(set)
#         for i, num in enumerate(arr):
#             index_list_by_num[num].add(i)
        
#         is_visit = set([0])
#         queue = deque([(0, 0)])
#         while queue:
#             curr_idx, depth = queue.popleft()
#             if curr_idx == n - 1:
#                 return depth 
#             curr_num = arr[curr_idx]
#             for next_idx in (curr_idx-1, curr_idx+1, *index_list_by_num[curr_num]):
#                 if 0<= next_idx < n and next_idx not in is_visit:
#                     is_visit.add(next_idx)
#                     queue.append((next_idx, depth+1))
from collections import deque, defaultdict
from typing import List


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0

        index_list_by_num = defaultdict(list)
        for i, num in enumerate(arr):
            index_list_by_num[num].append(i)
        start_queue = deque([[0, 0]])
        start_checker = {
            0: 0
        }
        end_queue = deque([[n - 1, 0]])
        end_checker = {
            n - 1: 0
        }

        def bfs_1_step(queue, checker1, checker2):
            curr, depth = queue.popleft()
            candidates = (curr-1, curr+1, *index_list_by_num[arr[curr]])
            for candidate in candidates:
                if 0 <= candidate < n and candidate not in checker1:
                    checker1[candidate] = depth + 1
                    if candidate in checker2:
                        return True, checker1[candidate] + checker2[candidate]
                    queue.append([candidate, depth + 1])
            return False, None

        while start_queue and end_queue:
            # bfs 1 step and check reachable
            reachable, answer = bfs_1_step(start_queue, start_checker, end_checker)
            if reachable:
                return answer
            
            reachable, answer = bfs_1_step(end_queue, end_checker, start_checker)
            if reachable:
                return answer
        return 0

            

