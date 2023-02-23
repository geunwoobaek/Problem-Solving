import heapq


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        captial_profits = sorted([c for c in zip(capital, profits)])
        hq = []
        for capital, profits in captial_profits:
            if k == 0:
                break

            while hq and k > 0 and w < capital:
                w += -heapq.heappop(hq)
                k -= 1

            if w < capital:
                break

            heapq.heappush(hq, -profits)

        while hq and k > 0:
            w += -heapq.heappop(hq)
            k -= 1
        return w
