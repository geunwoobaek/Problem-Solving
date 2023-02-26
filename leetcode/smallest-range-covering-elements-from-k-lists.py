## pointer 3개 두고
## [min(ai..), max(ai..)] (0<=i<3)
## if i==2
# i  =0, j=0 => [0,4]
# i = 1, j=0 => [0, 10]
# i = 0, j=1 => [4, 9]
# 작은거를 증가 시키는게 무조건 유리
# 0, 4 => 4,9 => 9,10 =>  10,12 ..


# 즉 가장 작은 포인터에 대해서 하나씩 옮기면 된다.
# 가장작은 녀석을 하나씩 빼낼 수 있어야함.
# max는 하나씩 넣을때마다 업데이트
import heapq
from math import inf
from typing import List


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        pointers = [0]*n
        max_num = max([nums[i][pointers[i]] for i in range(n)])
        pq = [[nums[i][pointers[i]], i] for i in range(n)]
        heapq.heapify(pq)
        answer_info = [inf, 0, inf]
        while pq:
            curr_min, nums_idx = heapq.heappop(pq)
            if max_num - curr_min < answer_info[0]:
                answer_info = [max_num - curr_min, curr_min, max_num]
            pointers[nums_idx] += 1
            if len(nums[nums_idx]) > pointers[nums_idx]:
                next_value = nums[nums_idx][pointers[nums_idx]]
                heapq.heappush(pq, [next_value, nums_idx])
                max_num = max(max_num, next_value)
            else:
                break
        return answer_info[1:]

print(Solution().smallestRange([[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]))