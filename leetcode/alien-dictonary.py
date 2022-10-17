from collections import defaultdict, deque
from typing import List

# Input: words = ["wrt","wrf","er","ett","rftt"]
# Output: "wertf"
# Example 2:

# w -> e -> r -> t -> f

# Input: words = ["z","x"]
# Output: "zx"
# Example 3:

# Input: words = ["z","x","z"]
# Output: ""



# Approach 1.
# BFS풀이
# 1. 현재문자 -> 다음문자 비교 변경이 되는 지점을 찾아서 inbound, outbound를 만든다.
# 2. inbound가 0인 문자를 찾아서 queue에 넣는다. 
# 3. inbound Size = 0일때, output에 넣어준다.
# 4. queue에서 하나씩 꺼내서 해당 문자의 outbound에 있는 문자들에서 inbound에서 현재 문자를 제거한다. 그 다음 queue에 넣어준다.
# 5. queue가 빌때까지 반복한다.
# 6. output을 리턴한다.
# ["wxqkj", "whqg", "cckgh", "cdxg", "cdxdt","cdht", "ktgxt","ktgch","ktdw","ktdc","jqw","jmc","jmg"]

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # inbound, outbound
        inbound = defaultdict(set)
        outbound = defaultdict(set)
        alphabet_set = set()
        for word in words:
            for c in word:
                alphabet_set.add(c)
        for idx in range(1,len(words)):

            word = words[idx]
            prev_word = words[idx-1]
            if len(prev_word) > len(word) and prev_word[:len(word)] == word:
                return ""
            # find first different character between prev_word and word
            a, b =None, None
            for c1, c2 in zip(prev_word, word):
                if c1 != c2:
                    a, b = c1, c2
                    break
            if a and b:
                inbound[b].add(a)
                outbound[a].add(b)
        # find inbound 0
        queue = deque([])
        for c in alphabet_set:
            if not inbound[c]:
                queue.append(c)
        # bfs
        output = []
        while queue:
            c = queue.popleft()
            if len(inbound[c]) == 0:
                output.append(c)
            for next_c in outbound[c]:
                inbound[next_c].remove(c)
                if not inbound[next_c]:
                    queue.append(next_c)
        return "".join(output) if len(output) == len(inbound) else ""

print(Solution().alienOrder(["wrt","wrf","er","ett","rftt"]) == "wertf")
print(Solution().alienOrder(["z","x"]) == "zx")
print(Solution().alienOrder(["z","x","z"]) == "")
print(Solution().alienOrder(["wxqkj","whqg","cckgh","cdxg","cdxdt","cdht","ktgxt","ktgch","ktdw","ktdc","jqw","jmc","jmg"]) == "whckjqgtdxm")