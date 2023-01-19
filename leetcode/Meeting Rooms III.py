# constraints
# 1 <= n <= 100
# 1 <= meetings.length <= 10^5
# meetings[i].length == 2
# 0 <= starti < endi <= 5 * 10^5
# All the values of starti are unique.
# Input: n = 2, meetings = [[0,10],[1,5],[2,7],[3,4]]
# Input: n = 2, meetings = [[0,10],[1,5],[2,7],[3,4]]
# Output: 0
# Explanation:
# - At time 0, both rooms are not being used. The first meeting starts in room 0.
# - At time 1, only room 1 is not being used. The second meeting starts in room 1.
# - At time 2, both rooms are being used. The third meeting is delayed.
# - At time 3, both rooms are being used. The fourth meeting is delayed.
# - At time 5, the meeting in room 1 finishes. The third meeting starts in room 1 for the time period [5,10).
# - At time 10, the meetings in both rooms finish. The fourth meeting starts in room 0 for the time period [10,11).
# Both rooms 0 and 1 held 2 meetings, so we return 0.
# using bruteforce
# 0 to end for loop and check if the meeting is in the range => timecomplexity O(n^2) = 5*10^10 = 50 billion
# sort starttime meetings
#
# using heap how? endtime of the meeting is the key, if the heap
# for i in range(start to end)
# now the time is i
# while current_meeting_pq[0][end_time] == time:
# pq.heappop()
# if there are delayroom insert current_meeting_pq and count+=1
# timecomplexity 5*10^5

# 했던 시도 1. 모든 타임라인을 다넣는다.



import heapq
from typing import List


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:

        meeting_counts = [0] * n
        meeting_ends_heap = []  # [end, room_id]
        free_rooms_heap = list(range(n))
        heapq.heapify(free_rooms_heap)

        meetings.sort()

        for start, end in meetings:
            while meeting_ends_heap and start >= meeting_ends_heap[0][0]:
                _, room_id = heapq.heappop(meeting_ends_heap)
                heapq.heappush(free_rooms_heap, room_id)

            delay = 0
            if free_rooms_heap:
                room_id = heapq.heappop(free_rooms_heap)
            else:
                delay = meeting_ends_heap[0][0] - start
                _, room_id = heapq.heappop(meeting_ends_heap)

            heapq.heappush(meeting_ends_heap, [end + delay, room_id])
            meeting_counts[room_id] += 1

        return meeting_counts.index(max(meeting_counts))

print(Solution().mostBooked(2, [[0,10],[1,5],[2,7],[3,4]]))