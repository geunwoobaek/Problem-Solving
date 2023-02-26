## 사과를 포함하는 rectangle 만든다
## 가로길이 * 세로 길이 한다.
import math


class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        n, m = len(pizza), len(pizza[0])
        prefixSum = [[0] * (m+1) for _ in range(n + 1)]
        for i in range(n-1, -1, -1):
            for j in range(m -1,-1, -1):
                prefixSum[i][j] = prefixSum[i][j + 1] + prefixSum[i + 1][j] - prefixSum[i + 1][j + 1] + (pizza[i][j] == 'A')

        @lru_cache(None)
        def getCount(y, x, k):
            if prefixSum[y][x] == 0:
                return 0
            if k == 0:
                return 1
            answer = 0
            for i in range(y + 1, n):
                if prefixSum[y][x] - prefixSum[i][x] > 0:
                    answer = (answer + getCount(i, x, k - 1)) % (10 ** 9 + 7)
            for j in range(x + 1, m):
                if prefixSum[y][x] - prefixSum[y][j] > 0:
                    answer = (answer + getCount(y, j, k - 1)) % (10 ** 9 + 7)
            return answer
        return getCount(0, 0, k - 1)

