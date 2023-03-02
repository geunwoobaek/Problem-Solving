

from collections import defaultdict
import heapq
from math import inf
from typing import List

# contraints:
# 1 <= n <= 100
# 0 <= roads.length <= n * (n - 1) / 2
# roads[i].length == 2
# 0 <= ui, vi <= n - 1
# dp[i][v] means the minimum edit distance from the start to the i-th node in the targetPath, and the current node is v.
# dp[i][v] = min(dp[i - 1][u] + cost(u, v)) for all u in roads[v]
# time complexity: O(n^2 * m)
# what is m? m is the length of the targetPath
class Solution:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:

        name_to_idx = {name: i for i, name in enumerate(names)}
        targetPath = [name_to_idx[name] if name in name_to_idx else -1 for name in targetPath]
        names = [name_to_idx[name] for name in names]
        graph = defaultdict(set)
        for u, v in roads:
            graph[u].add(v)
            graph[v].add(u)

        dp = [[inf]*n for _ in range(len(targetPath))]
        for v in range(n):
            dp[0][v] = int(names[v] != targetPath[0])
        for i in range(1, len(targetPath)):
            for v in range(n):
                for u in graph[v]:
                    dp[i][v] = min(dp[i][v], dp[i - 1][u] + int(names[v] != targetPath[i]))

        # trace
        end_node = dp[-1].index(min(dp[-1]))
        min_path = [end_node]
        for i in range(len(targetPath) - 1, 0, -1):
            for u in graph[end_node]:
                if dp[i][end_node] == dp[i - 1][u] + int(names[end_node] != targetPath[i]):
                    min_path.append(u)
                    end_node = u
                    break
        return min_path[::-1]



## leetcode Solution
class Solution:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str],
                    targetPath: List[str]) -> List[int]:
        dp = [[len(targetPath) + 1] * n for i in range(len(targetPath))]
        p = [[None] * n for i in range(len(targetPath))]
        # initialize DP
        dp[0] = [names[i] != targetPath[0] for i in range(n)]
        # calculate DP
        for i in range(1, len(targetPath)):
            for road in roads:
                # consider both edges (u, v) and (v, u)
                for j in range(2):
                    u = road[j]
                    v = road[j ^ 1]
                    cur = dp[i - 1][u] + (names[v] != targetPath[i])
                    if cur < dp[i][v]:
                        dp[i][v] = cur
                        p[i][v] = u
        # the last vertex in the path
        v = dp[-1].index(min(dp[-1]))
        ans = [v]
        for i in range(len(targetPath) - 1, 0, -1):
            # the previous vertex in the path
            v = p[i][v]
            ans.append(v)
        return reversed(ans)
