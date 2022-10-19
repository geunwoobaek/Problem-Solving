# https://leetcode.com/problems/amount-of-new-area-painted-each-day/
class SegmentTree:
    def __init__(self, N: int):
        self.tree = [0] * N
    
    def increment(self, qlo: int, qhi: int, lo: int, hi: int, pos: int) -> int:
        total = hi - lo + 1
        
        if self.tree[pos] == total:     # if the node is full, return 0
            return 0
        
        if qlo <= lo <= hi <= qhi:      # case 1, total overlap
            missing = total - self.tree[pos]
            self.tree[pos] = total
            return missing
        elif qlo > hi or qhi < lo:      # case 2, NO overlap
            return 0
        
        mid = lo + (hi - lo) // 2       # case 3, partial overlap
        left = self.increment(qlo, qhi, lo, mid, 2 * pos + 1)
        right = self.increment(qlo, qhi, mid + 1, hi, 2 * pos + 2)
        self.tree[pos] += left + right
        return left + right
                

class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        
        N = max(r for _, r in paint)
        
        tree = SegmentTree(4 * N)
        worklog = []
        
        for qlo, qhi in paint:
            work = tree.increment(qlo, qhi-1, 0, N, 0)
            worklog.append(work)
            
        return worklog