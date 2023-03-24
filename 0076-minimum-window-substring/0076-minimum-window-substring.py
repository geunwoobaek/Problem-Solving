# bruteforce  모든 문자열을 시작점으로 해서 check 10^10 tle
# sortedlist ADOBEC ABC
from collections import Counter, deque
import math


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counter = Counter(t)
        total_counter = len(t)
        queue = deque([])
        ans = math.inf
        min_start_idx = 0
        for idx, c in enumerate(s):
            if c in t_counter:
                t_counter[c] -= 1
            if c in t_counter and t_counter[c] >= 0:
                total_counter -= 1
            queue.append([c, idx])
            while total_counter == 0 and queue:
                if len(queue) < ans:
                    ans = len(queue)
                    min_start_idx = queue[0][1]
                curr, _ = queue.popleft()
                if curr in t_counter:
                    t_counter[curr] += 1
                if curr in t_counter and t_counter[curr] > 0:
                    total_counter += 1
        if ans == math.inf:
            return ""
        return s[min_start_idx: min_start_idx + ans]



