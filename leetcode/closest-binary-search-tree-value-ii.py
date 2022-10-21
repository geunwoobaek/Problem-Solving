# Definition for a binary tree node.
# 1 <= k <= n <= 104.
# 0 <= Node.val <= 109
# -109 <= target <= 109
 

# Follow up: Assume that the BST is balanced. Could you solve it in less than O(n) runtime (where n = total nodes)?
# Approach 1 
# first find closet node
# using priority queue from closet node worstcase 
# heapify n => n
from collections import deque
import heapq
import math
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        
        visited = set()
        queue = []
        def insertAllNode(currNode):
            if not currNode:
                return
            if currNode.val not in visited:
                visited.add(currNode.val)
                heapq.heappush(queue,(abs(currNode.val - target), currNode.val))
                insertAllNode(currNode.left)
                insertAllNode(currNode.right)
        insertAllNode(root)
        return [heapq.heappop(queue)[1] for _ in range(k)]
# test [4,2,5,1,3], 3.714286, 2   = [4, 3]
print(Solution().closestKValues(TreeNode(4,TreeNode(2,TreeNode(1),TreeNode(3)), TreeNode(5)),3.71,2))
print(Solution().closestKValues(TreeNode(1,None,TreeNode(2)),1.9,1))
    
        