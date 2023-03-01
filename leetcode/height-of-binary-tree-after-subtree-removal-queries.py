# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# brute force 방식으로 풀게 되면 query 당 dfs 돌려서 O(N)발생하고
# query len = O(N), so O(N) * O(N) 발생하게된다
# optimized solution


# approach 1
# solve 현재 sibling들의 정보 depth, height를 이용해서 문제풀기
# 예를들어 현재 노드의 depth가 2라면, 해당 노드를 제외한 depth 2에 해당하는 maximum height를 가지는 노드를 찾아야한다.
from collections import defaultdict, deque


class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        heights = {}

        def get_height(node):
            if not node:
                return -1

            if node.val in heights:
                return heights[node.val]

            heights[node.val] = 1 + \
                max(get_height(node.left), get_height(node.right))
            return heights[node.val]
        get_height(root)

        queue = deque([[root, 0]])
        depth_from_node = {}
        nodes_from_depth = defaultdict(list)
        while queue:
            node, depth = queue.popleft()
            depth_from_node[node.val] = depth
            nodes_from_depth[depth].append(node.val)
            if node.left:
                queue.append([node.left, depth + 1])
            if node.right:
                queue.append([node.right, depth + 1])

        for _, nodes in nodes_from_depth.items():
            nodes.sort(key=lambda x: -heights[x])

        res = []
        for node in queries:
            depth = depth_from_node[node]
            nodes = nodes_from_depth[depth]
            curr_res = 0
            if len(nodes) == 1:
                curr_res = depth - 1
            elif nodes[0] == node:
                curr_res = heights[nodes[1]] + depth
            else:
                curr_res = heights[nodes[0]] + depth
            res.append(curr_res)
        return res

    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        res = defaultdict(int)

        def dfs(root, h, maxh):
            if not root:
                return maxh
            res[root.val] = max(res[root.val], maxh)
            root.left, root.right = root.right, root.left
            return dfs(root.right, h + 1, dfs(root.left, h + 1, max(maxh, h)))

        dfs(root, 0, 0)
        dfs(root, 0, 0)
        return [res[q] for q in queries]


# approach 2 preorder traversal