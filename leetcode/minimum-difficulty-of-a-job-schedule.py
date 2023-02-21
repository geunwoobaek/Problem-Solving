from functools import lru_cache
import math
from typing import List

## [7,1,7,1,7,1] day = 3
## [1,7,7,7,2] day = 2
## [2,7,7,7,1] day = 2
## k exists (current_idx <= k <= end of day - remaining_days)
## dp[current_idx][remaining_days] = max(diff[current_idx] ~ diff[k]) + dp[k+1][remaining_days-1]



class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1

        @lru_cache(None)
        def dp(curr_idx, remaining_days):
            answer = math.inf
            curr_max_value = 0
            if remaining_days == 1:
                return max(jobDifficulty[curr_idx:])

            for end_idx in range(curr_idx, n - remaining_days + 1):
                curr_max_value = max(curr_max_value, jobDifficulty[end_idx])
                answer = min(answer, curr_max_value + dp(end_idx + 1, remaining_days - 1))
            return answer
        return dp(0, d)


print(Solution().minDifficulty([6,5,4,3,2,1], 2))
